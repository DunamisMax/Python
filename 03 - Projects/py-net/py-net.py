#!/usr/bin/env python3
import platform
import socket
import subprocess
import sys
import ssl
from datetime import datetime
from urllib.request import Request, urlopen


def ping_host(host: str, count: int = 4) -> None:
    """Ping a host using the system ping command."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    print(f"\nPinging {host} with {count} packets...\n")
    try:
        subprocess.check_call(["ping", param, str(count), host])
    except FileNotFoundError:
        print("Error: 'ping' command not found on this system.")
    except subprocess.CalledProcessError as e:
        print(f"Ping command failed with exit code {e.returncode}")


def traceroute_host(host: str) -> None:
    """Traceroute to a host using the system traceroute/tracert command."""
    traceroute_cmd = (
        "tracert" if platform.system().lower() == "windows" else "traceroute"
    )
    print(f"\nRunning {traceroute_cmd} on {host}...\n")
    try:
        subprocess.check_call([traceroute_cmd, host])
    except FileNotFoundError:
        print(f"Error: '{traceroute_cmd}' command not found on this system.")
    except subprocess.CalledProcessError as e:
        print(f"{traceroute_cmd} command failed with exit code {e.returncode}")


def dns_lookup(host: str) -> None:
    """Resolve a hostname to its IP addresses."""
    print(f"\nPerforming DNS lookup on {host}...\n")
    try:
        addr_info = socket.getaddrinfo(host, None)
        unique_ips = set([info[4][0] for info in addr_info])
        print(f"DNS Lookup Results for {host}:")
        for ip in unique_ips:
            print(f" - {ip}")
    except socket.gaierror as e:
        print(f"DNS resolution failed: {e}")


def port_scan(host: str, start: int, end: int) -> None:
    """Scan a range of TCP ports on a host."""
    print(f"\nScanning {host} from port {start} to {end}...\n")
    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            try:
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"Port {port} is OPEN")
            except socket.error:
                pass


def fetch_http_headers(url: str) -> None:
    """Fetch and display HTTP headers from a given URL."""
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "http://" + url
    print(f"\nFetching HTTP headers from {url}...\n")
    req = Request(url, method="HEAD")
    try:
        with urlopen(req, timeout=5) as response:
            print(f"HTTP Headers for {url}:")
            for header, value in response.headers.items():
                print(f"{header}: {value}")
    except Exception as e:
        print(f"Failed to fetch headers from {url}: {e}")


def directory_brute_force(url: str, wordlist_file: str) -> None:
    """Try a list of directories against a given URL."""
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "http://" + url

    print(
        f"\nStarting directory brute force on {url} using wordlist {wordlist_file}...\n"
    )
    try:
        with open(wordlist_file, "r") as f:
            dirs = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Failed to read wordlist file: {e}")
        return

    for d in dirs:
        test_url = url.rstrip("/") + "/" + d
        req = Request(test_url, method="HEAD")
        try:
            with urlopen(req, timeout=2) as response:
                if response.status in (200, 301, 302):
                    print(f"Found: {test_url} (Status: {response.status})")
        except:
            pass


def whois_lookup(domain: str) -> None:
    """Perform a WHOIS lookup for a given domain using the system 'whois' command."""
    print(f"\nPerforming WHOIS lookup for {domain}...\n")
    try:
        output = subprocess.check_output(
            ["whois", domain], stderr=subprocess.STDOUT, universal_newlines=True
        )
        print(output)
    except FileNotFoundError:
        print(
            "Error: 'whois' command not found on this system. Please install whois or run this on a platform that provides it."
        )
    except subprocess.CalledProcessError as e:
        print(
            f"WHOIS command failed with exit code {e.returncode}. Output:\n{e.output}"
        )


def reverse_dns_lookup(ip: str) -> None:
    """Perform a reverse DNS lookup on an IP address."""
    print(f"\nPerforming reverse DNS lookup on {ip}...\n")
    try:
        host, aliases, addresses = socket.gethostbyaddr(ip)
        print(f"Host: {host}")
        if aliases:
            print("Aliases:")
            for alias in aliases:
                print(f" - {alias}")
        if addresses:
            print("Addresses:")
            for addr in addresses:
                print(f" - {addr}")
    except socket.herror as e:
        print(f"Reverse DNS lookup failed: {e}")
    except socket.gaierror as e:
        print(f"Reverse DNS lookup failed: {e}")


def ssl_cert_expiration(host: str, port: int = 443) -> None:
    """Check the SSL certificate expiration date for a given host."""
    print(f"\nChecking SSL certificate expiration for {host}:{port}...\n")
    context = ssl.create_default_context()
    try:
        with socket.create_connection((host, port), timeout=5) as conn:
            with context.wrap_socket(conn, server_hostname=host) as ssl_sock:
                cert = ssl_sock.getpeercert()
                # 'notAfter' typically looks like "Aug  5 12:00:00 2025 GMT"
                not_after = cert.get("notAfter")
                if not_after:
                    expires = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
                    print(f"Certificate for {host} expires on: {expires}")
                    days_to_expire = (expires - datetime.utcnow()).days
                    print(f"Days until expiration: {days_to_expire}")
                else:
                    print("Could not retrieve expiration date from certificate.")
    except Exception as e:
        print(f"Failed to retrieve SSL certificate: {e}")


def arp_neighbor_discovery():
    """
    Lists devices discovered on the local network by querying the ARP cache.
    This relies on external commands ('arp -a' or 'ip neigh show') and may not be fully cross-platform.
    """
    print("\nAttempting ARP-based neighbor discovery...\n")
    # Try `arp -a` first
    try:
        output = subprocess.check_output(
            ["arp", "-a"], stderr=subprocess.STDOUT, universal_newlines=True
        )
        print("=== ARP Table (arp -a) ===")
        print(output.strip())
    except FileNotFoundError:
        # If `arp` not found, try `ip neigh show`
        try:
            output = subprocess.check_output(
                ["ip", "neigh", "show"],
                stderr=subprocess.STDOUT,
                universal_newlines=True,
            )
            print("=== Neighbor Discovery (ip neigh show) ===")
            print(output.strip())
        except FileNotFoundError:
            print(
                "Error: Neither 'arp' nor 'ip neigh' command found. Cannot perform ARP neighbor discovery."
            )
        except subprocess.CalledProcessError as e:
            print(f"Failed to run 'ip neigh show': {e.output}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run 'arp -a': {e.output}")


def mdns_service_discovery():
    """
    Attempt to list mDNS/Bonjour services on the local network using 'avahi-browse'.
    This relies on avahi-browse being installed (e.g., on Linux).
    """
    print("\nAttempting mDNS/DNS-SD service discovery (using avahi-browse)...\n")
    try:
        output = subprocess.check_output(
            ["avahi-browse", "-alr"], stderr=subprocess.STDOUT, universal_newlines=True
        )
        print("=== mDNS Services (avahi-browse) ===")
        print(output.strip())
    except FileNotFoundError:
        print(
            "Error: 'avahi-browse' command not found. Please install avahi-tools or run on a system with it available."
        )
    except subprocess.CalledProcessError as e:
        print(f"Failed to run 'avahi-browse': {e.output}")


def netbios_discovery():
    """
    Attempt to discover NetBIOS names on the local network using 'nmblookup'.
    This tries a broadcast query to list all names on the subnet.
    """
    print("\nAttempting NetBIOS name discovery (using nmblookup)...\n")
    try:
        # '-S' to list machine details, '*' to query all.
        output = subprocess.check_output(
            ["nmblookup", "-S", "*"], stderr=subprocess.STDOUT, universal_newlines=True
        )
        print("=== NetBIOS Names (nmblookup) ===")
        print(output.strip())
    except FileNotFoundError:
        print(
            "Error: 'nmblookup' command not found. Please install Samba tools or run on a system that provides it."
        )
    except subprocess.CalledProcessError as e:
        print(f"Failed to run 'nmblookup': {e.output}")


def prompt_for_host() -> str:
    while True:
        host = input("Enter the hostname or IP address: ").strip()
        if host:
            return host
        print("Invalid input. Please provide a valid hostname or IP.")


def prompt_for_url() -> str:
    while True:
        url = input("Enter the URL (with or without http/https): ").strip()
        if url:
            return url
        print("Invalid input. Please provide a valid URL.")


def prompt_for_count(default=4) -> int:
    while True:
        count_str = input(f"Enter the number of packets [{default}]: ").strip()
        if not count_str:
            return default
        if count_str.isdigit() and int(count_str) > 0:
            return int(count_str)
        print("Invalid input. Please enter a positive integer.")


def prompt_for_port_range(default_start=1, default_end=1024) -> (int, int):
    while True:
        ports_str = input(
            f"Enter port or port range (e.g., '80' or '20-80') [{default_start}-{default_end}]: "
        ).strip()
        if not ports_str:
            return (default_start, default_end)
        if "-" in ports_str:
            parts = ports_str.split("-", 1)
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                start, end = int(parts[0]), int(parts[1])
                if 0 < start <= end <= 65535:
                    return (start, end)
        else:
            if ports_str.isdigit():
                p = int(ports_str)
                if 0 < p <= 65535:
                    return (p, p)
        print(
            "Invalid input. Please enter a valid port or range, e.g. '80' or '20-80'."
        )


def prompt_for_wordlist() -> str:
    while True:
        wordlist = input("Enter the path to the wordlist file: ").strip()
        if wordlist:
            return wordlist
        print("Invalid input. Please provide a valid file path.")


def main_menu():
    print("\n============================")
    print("   Network Toolkit Menu")
    print("============================")
    print("1) Ping a host")
    print("2) DNS lookup")
    print("3) Port scan")
    print("4) Traceroute")
    print("5) HTTP Headers")
    print("6) Directory brute force")
    print("7) WHOIS Lookup")
    print("8) Reverse DNS Lookup")
    print("9) SSL Certificate Expiration Check")
    print("10) ARP / Neighbor Discovery")
    print("11) mDNS/DNS-SD Service Discovery")
    print("12) NetBIOS Discovery")
    print("13) Quit")
    print("============================")


def run_tool():
    while True:
        main_menu()
        choice = input("Select an option (1-7): ").strip()
        if choice == "1":
            host = prompt_for_host()
            count = prompt_for_count()
            ping_host(host, count)
        elif choice == "2":
            host = prompt_for_host()
            dns_lookup(host)
        elif choice == "3":
            host = prompt_for_host()
            start, end = prompt_for_port_range()
            port_scan(host, start, end)
        elif choice == "4":
            host = prompt_for_host()
            traceroute_host(host)
        elif choice == "5":
            url = prompt_for_url()
            fetch_http_headers(url)
        elif choice == "6":
            url = prompt_for_url()
            wordlist = prompt_for_wordlist()
            directory_brute_force(url, wordlist)
        elif choice == "7":
            domain = prompt_for_host()
            whois_lookup(domain)
        elif choice == "8":
            ip = prompt_for_host()
            reverse_dns_lookup(ip)
        elif choice == "9":
            host = prompt_for_host()
            port_str = input("Enter port [443]: ").strip()
            port = int(port_str) if port_str.isdigit() else 443
            ssl_cert_expiration(host, port)
        elif choice == "10":
            arp_neighbor_discovery()
        elif choice == "11":
            mdns_service_discovery()
        elif choice == "12":
            netbios_discovery()
        elif choice == "13":
            print("Exiting the network toolkit. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice, please try again.")

        input("\nPress Enter to return to the main menu...")


if __name__ == "__main__":
    run_tool()
