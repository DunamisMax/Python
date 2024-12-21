#!/usr/bin/env python3
import socket
import subprocess
import sys
import shlex
import time
from concurrent.futures import ThreadPoolExecutor


def run_command(cmd):
    """Run a shell command and return its output or an error message."""
    try:
        output = subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT, text=True
        )
        return output
    except FileNotFoundError:
        return f"Command not found: {cmd.split()[0]}"
    except subprocess.CalledProcessError as e:
        return e.output.strip()


def is_ip_address(host):
    """Check if the given host string is a valid IP address."""
    try:
        socket.inet_pton(socket.AF_INET, host)
        return True
    except OSError:
        pass
    try:
        socket.inet_pton(socket.AF_INET6, host)
        return True
    except OSError:
        pass
    return False


def dns_lookup(host):
    """Perform a DNS lookup to get the IP address of the host."""
    try:
        ip = socket.gethostbyname(host)
        return f"DNS Lookup for {host}:\n  IP Address: {ip}\n"
    except socket.gaierror as e:
        return f"DNS Lookup for {host} failed:\n  {e}\n"


def reverse_dns_lookup(host):
    """Perform a reverse DNS lookup if possible."""
    try:
        ip = socket.gethostbyname(host)
        name, aliases, _ = socket.gethostbyaddr(ip)
        return (
            f"Reverse DNS Lookup for {ip}:\n"
            f"  Hostname: {name}\n"
            f"  Aliases: {', '.join(aliases) if aliases else 'None'}\n"
        )
    except (socket.herror, socket.gaierror) as e:
        return f"Reverse DNS Lookup for {host} failed:\n  {e}\n"


def ping_host(host, count=4, timeout=2):
    """Ping the host using the system ping command."""
    if sys.platform.startswith("win"):
        # Windows ping: -n count, -w timeout_in_ms
        cmd = f"ping -n {count} -w {timeout*1000} {shlex.quote(host)}"
    else:
        # Unix-like ping: -c count, -W timeout_in_sec
        cmd = f"ping -c {count} -W {timeout} {shlex.quote(host)}"
    output = run_command(cmd)
    if (
        "Ping request could not find host" in output
        or "not known" in output.lower()
        or "could not resolve" in output.lower()
    ):
        return f"Ping {host} failed:\n{output}\n"
    return f"Ping {host}:\n{output}\n"


def traceroute_host(host, max_hops=30):
    """Perform a traceroute using the appropriate system command."""
    if sys.platform.startswith("win"):
        # On Windows, use 'tracert'
        cmd = f"tracert -d -h {max_hops} {shlex.quote(host)}"
    else:
        # On Unix-like systems, use 'traceroute'
        cmd = f"traceroute -m {max_hops} {shlex.quote(host)}"
    output = run_command(cmd)
    if "not recognized" in output or "not found" in output:
        return f"Traceroute to {host} failed:\n{output}\n"
    return f"Traceroute to {host}:\n{output}\n"


def port_scan(host, port, timeout=2):
    """Check if a TCP port is open by attempting to connect."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.connect((host, port))
        sock.close()
        return f"Port Scan {host}:{port}:\n  Port {port} is OPEN\n"
    except socket.timeout:
        return f"Port Scan {host}:{port}:\n  Connection timed out. Port might be FILTERED/CLOSED.\n"
    except (ConnectionRefusedError, socket.gaierror):
        return f"Port Scan {host}:{port}:\n  Connection refused or host unreachable. Port is CLOSED.\n"
    finally:
        sock.close()


def whois_lookup(host):
    """Perform a WHOIS lookup if whois is available and host is not an IP."""
    if is_ip_address(host):
        return f"WHOIS Lookup for {host} skipped: target is an IP, not a domain.\n"

    cmd = f"whois {shlex.quote(host)}"
    output = run_command(cmd)
    # Check if whois command was not found or returned an error
    if "Command not found:" in output or "not recognized" in output.lower():
        return f"WHOIS Lookup for {host} failed:\n  'whois' command not available on this system.\n"
    if "No match for" in output or "NOT FOUND" in output.upper():
        return f"WHOIS Lookup for {host}:\n  No WHOIS data found.\n"
    return f"WHOIS Lookup for {host}:\n{output}\n"


def latency_test(host, port=None, attempts=5, timeout=2):
    """Measure approximate network latency by timing TCP connection attempts."""
    if port is None:
        # Default to port 80 if no port provided
        port = 80

    latencies = []
    for i in range(attempts):
        start_time = time.time()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
            sock.close()
            elapsed = time.time() - start_time
            latencies.append(elapsed * 1000.0)  # convert to ms
        except Exception:
            # If connection fails, record it as None or skip
            latencies.append(None)
        finally:
            sock.close()

    successful_latencies = [l for l in latencies if l is not None]
    if not successful_latencies:
        return f"Latency Test for {host}:{port}:\n  All connection attempts failed.\n"

    avg_latency = sum(successful_latencies) / len(successful_latencies)
    return (
        f"Latency Test for {host}:{port} ({attempts} attempts):\n"
        f"  Successful attempts: {len(successful_latencies)}\n"
        f"  Average latency: {avg_latency:.2f} ms\n"
    )


def main():
    # Prompt user for input
    user_input = input("Enter hostname/IP [and optional port]: ").strip()
    if not user_input:
        print("No input provided. Exiting.")
        sys.exit(1)

    parts = user_input.split()
    host = parts[0]
    port = None
    if len(parts) > 1:
        try:
            port = int(parts[1])
        except ValueError:
            print("Invalid port specified. Exiting.")
            sys.exit(1)

    # Prepare tasks
    tasks = [
        (dns_lookup, (host,)),
        (reverse_dns_lookup, (host,)),
        (ping_host, (host,)),
        (traceroute_host, (host,)),
        (whois_lookup, (host,)),
        (latency_test, (host, port)),
    ]
    if port is not None:
        tasks.append((port_scan, (host, port)))

    # Run tasks in parallel
    results = []
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(func, *args) for func, args in tasks]
        for future in futures:
            results.append(future.result())

    # Print results
    print("\n" + "=" * 60)
    print("NETWORK TOOL RESULTS")
    print("=" * 60 + "\n")
    for r in results:
        print(r.strip() + "\n")


if __name__ == "__main__":
    main()
