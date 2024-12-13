# Hacking Cheat Sheet

**Disclaimer:**
All activities described here must be conducted only with proper authorization and for legitimate security assessments. Always adhere to your organization’s rules, clients’ contracts, and applicable legal regulations. Unauthorized hacking is illegal and unethical.

---

## 1. Ethical Hacking Methodology & Mindset

**Core Principles:**

- **Obtain Proper Authorization:** Written permission from the target owner is mandatory.
- **Scope Definition:** Clearly define in-scope hosts, applications, and testing boundaries.
- **Non-Destructive Testing:** Avoid disruptive attacks or unnecessary downtime.
- **Confidential Reporting:** Securely handle sensitive data and responsibly disclose vulnerabilities.

**Pentesting Methodology (Common Frameworks):**

1. **Information Gathering & Reconnaissance:** Identify target surfaces, technologies, and entry points.
2. **Vulnerability Analysis:** Map known vulnerabilities and assess exploitability.
3. **Exploitation:** Confirm vulnerabilities by exploiting them within allowed scope.
4. **Post-Exploitation & Lateral Movement:** Escalate privileges, move within the network.
5. **Reporting & Remediation:** Document findings, provide actionable fixes.

**Standards & Guidelines:**

- **OWASP Testing Guide:** For web application tests.
- **NIST SP 800-115:** Technical guide to information security testing.
- **PTES (Penetration Testing Execution Standard):** Methodology for thorough engagements.

---

## 2. Reconnaissance & Information Gathering

**Key Objectives:**

- Identify hosts, IP ranges, domains, subdomains.
- Gather server technologies, banners, and platform versions.
- Map known endpoints, directories, parameters.

**Common Tools & Techniques:**

- **Passive Recon:** WHOIS lookups, DNS enumeration, certificate transparency logs, OSINT (Open-Source Intelligence) sources, social media, LinkedIn.
- **Active Recon:** Network scans, service fingerprinting, port enumeration.

**Command-Line Utilities:**

- `whois domain.com`
- `dig @dnsserver domain.com ANY`
- `nslookup`, `host`, `dnsrecon`, `dnsenum` for DNS enumeration
- `theHarvester`, `amass` for subdomain enumeration
- `curl -I https://example.com` for banner grabbing.

**Python Snippets for Recon:**

```python
import socket

host = "example.com"
ip = socket.gethostbyname(host)
print(f"{host} resolves to {ip}")
```

**HTTP Enumerations & Fingerprinting:**

- Use `requests` library in Python to fetch headers, examine response codes, identify server types.

```python
import requests

resp = requests.get("https://example.com")
print(resp.headers)
```

---

## 3. Scanning & Enumeration

**Network Scanning:**

- **Nmap:** Gold standard for host discovery, port scanning, service/version detection.

```bash
nmap -sV -sC -oN scan.txt target.com
```

**Service Enumeration:**

- **SMB:** `smbclient`, `enum4linux`
- **FTP:** `ftp`, `nmap` scripts
- **SSH:** Banner grabbing, key exchange info
- **HTTP:** `nikto`, `dirb`, `gobuster` for directory busting, `whatweb` for web fingerprinting.

**Python + Scapy for Packet Crafting & Analysis:**

```python
from scapy.all import *

# Send SYN packet and receive SYN-ACK for port scanning
syn_packet = IP(dst="1.2.3.4")/TCP(dport=80,flags="S")
resp = sr1(syn_packet,timeout=1)
if resp and resp.haslayer(TCP) and resp[TCP].flags == 0x12:
    print("Port 80 is open!")
```

---

## 4. Vulnerability Analysis

**Common Vulnerability Types:**

- **Web:** SQL injection, XSS, CSRF, SSRF, RCE, file inclusion, IDOR.
- **Network:** Unpatched services, weak credentials, misconfigurations.
- **Application Logic Flaws:** Broken access controls, insecure direct object references.
- **Cryptographic Issues:** Weak ciphers, improper key management.

**Automated Vulnerability Scanners:**

- **OpenVAS, Nessus, Qualys:** Network scanning.
- **Burp Suite, OWASP ZAP:** Web application scanning and fuzzing.
- **Nmap NSE Scripts:** Specialized checks for known CVEs and misconfigs.

**Python for Custom Vulnerability Checks:**

```python
import requests

url = "https://vulnerable-site.com/search"
payload = "' OR '1'='1"
resp = requests.get(url, params={"q": payload})
if "results" in resp.text.lower():
    print("Potential SQL injection found!")
```

---

## 5. Exploitation

**General Approach:**

- Confirm vulnerability feasibility.
- Use exploit frameworks or write custom exploits.
- Exploit only in authorized scope, minimize damage.

**Popular Exploit Frameworks:**

- **Metasploit Framework:** Rapid exploitation and payload delivery.

```bash
msfconsole
use exploit/linux/http/...
set RHOSTS target
set RPORT 80
run
```

**Web Exploitation Tools:**

- **SQLmap:** Automated SQL injection exploitation.
- **XSStrike:** XSS testing suite.

**Python Exploit Snippets:**

```python
# Example: Blind SQL injection timing test
import requests
import time

url = "http://target.com/item?id="
injection = "1' AND SLEEP(5)--"
start = time.time()
resp = requests.get(url + injection)
end = time.time()

if (end - start) > 5:
    print("Target is vulnerable to blind SQL injection!")
```

---

## 6. Password Attacks & Cracking

**Warning:** Use only on systems you own or have explicit permission to test.

**Password Attack Methods:**

- **Brute Force & Dictionary Attacks:** Guessing credentials using wordlists.
- **Rainbow Tables & Hash Cracking:** Using precomputed hash tables or `hashcat`, `John the Ripper`.

**Python for Brute Force (with caution):**

```python
import requests

login_url = "https://target.com/login"
for pwd in open("wordlist.txt"):
    pwd = pwd.strip()
    resp = requests.post(login_url, data={"user":"admin", "pass":pwd})
    if "Welcome" in resp.text:
        print(f"Password found: {pwd}")
        break
```

**Hash Cracking Tools:**

- `hashcat` (GPU accelerated)
- `john` (John the Ripper)

---

## 7. Post-Exploitation & Privilege Escalation

**Once In, Pivot and Elevate Privileges:**

- **Enumerate System Info:** OS version, installed software, running processes.
- **Check for Misconfigurations:** Writable files in PATH, SUID binaries, weak service configurations.
- **Escalation Techniques:** Exploit kernel vulnerabilities, misconfigured cron jobs, stored credentials.

**Linux PrivEsc Checks:**

- `sudo -l` (check allowed commands)
- `linPEAS`, `LinEnum`, `linux-smart-enumeration` scripts for thorough enumeration.

**Windows PrivEsc:**

- Check registry misconfigurations, unquoted service paths, alwaysInstallElevated keys.
- Tools: `winPEAS`, `PowerUp`, `SharpUp`.

**Python Post-Exploitation Utility:**

```python
import os

# Example: List processes (post-exploitation)
processes = os.popen("ps aux").read()
print(processes)
```

---

## 8. Lateral Movement & Persistence

**Moving Through the Network:**

- **Pivoting:** Use compromised host as a pivot to access internal subnets.
- **SSH Tunnels & Proxies:** Forward ports through compromised machines.
- **Credential Harvesting:** Extracting tokens, passwords, keys for further access.

**Persistence Techniques (Ethically!):**

- Scheduled tasks, startup scripts, service modifications on owned systems during a red-team scenario.

**Python Port Forwarder:**

```python
import socket

def forward(local_port, remote_host, remote_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", local_port))
    s.listen(1)
    while True:
        client, addr = s.accept()
        remote = socket.create_connection((remote_host, remote_port))
        # Forward traffic between client and remote
```

---

## 9. Wireless & Network Attacks

**Authorization & Legality:**

- Only pentest wireless networks you have permission for.

**Tools:**

- **Aircrack-ng Suite:** Capturing handshakes, cracking WPA keys.
- **Kismet:** Wireless network discovery and monitoring.

**Bluetooth & IoT:**

- **BlueZ, gatttool:** For Bluetooth enumeration.
- **Shodan & Censys:** IoT device discovery (OSINT-based, passive).

---

## 10. Web Application Testing

**OWASP Top 10:**

- Injections (SQL, NoSQL, OS Command)
- Broken Auth/Session Management
- Sensitive Data Exposure
- XML External Entities (XXE)
- Broken Access Control
- Security Misconfigurations
- Cross-Site Scripting (XSS)
- Insecure Deserialization
- Using Vulnerable Components
- Insufficient Logging & Monitoring

**Burp Suite & OWASP ZAP:**

- Intercept requests, modify parameters, test input validation.
- Use fuzzers to identify hidden parameters, directories.

**Python for Web Vulnerability Testing:**

```python
import requests

urls = ["http://target.com/search?q=", "http://target.com/item?id="]
payloads = ["' OR '1'='1", "<script>alert(1)</script>"]
for url in urls:
    for p in payloads:
        resp = requests.get(url + p)
        if "syntax error" in resp.text or "<script>" in resp.text:
            print(f"Potential vulnerability at: {url+p}")
```

---

## 11. API & Microservices Testing

**Key Areas:**

- Check for broken authentication (tokens, JWT).
- Rate limiting bypass attempts.
- JSON injection, GraphQL injections, parameter tampering.

**Testing Tools:**

- `Postman`, `Insomnia`, `Burp Suite`, `sqlmap` with REST APIs, `graphqlmap`.

---

## 12. Cloud & Container Security

**Cloud Pentesting:**

- Check IAM misconfigurations (AWS IAM policies, GCP IAM roles).
- Publicly exposed S3 buckets, unsecured blob storage.
- Use `awscli`, `gcloud`, `azcli` and cloud exploitation frameworks (Pacu for AWS).

**Container & Kubernetes Security:**

- Check Dockerfiles for secrets, insecure images.
- `kube-hunter` for Kubernetes cluster vulnerabilities.
- Check RBAC misconfigurations, exposed kubelet APIs.

---

## 13. Defensive Evasion & Anti-Detection Techniques (Red Teaming)

**Warning:**
These techniques should only be used in authorized red team engagements. Understand blue team defenses to test detection capabilities.

**Concepts:**

- Obfuscate payloads, encode commands.
- Modify indicators in memory, rotate C2 channels.
- Use signed binaries or living-off-the-land binaries (LOLBins).

**Python Encoding Example:**

```python
import base64

payload = b"cmd /c whoami"
encoded = base64.b64encode(payload)
print(encoded)
```

---

## 14. Reporting & Documentation

**Vulnerability Documentation:**

- **Evidence Gathering:** Screenshots, request/response logs, exploit steps.
- **Risk Assessment:** CVSS scoring, business impact analysis.
- **Actionable Remediation:** Detailed instructions to fix issues.

**Reporting Frameworks & Templates:**

- Use Markdown or Asciidoc for clean formatting.
- Tools like Dradis, Faraday, or Serpico to manage reports.
- Include Executive Summary, Technical Details, Proof-of-Concept, and Recommendations.

---

## 15. Compliance & Legal Considerations

**Know the Legal Boundaries:**

- Laws like the Computer Fraud and Abuse Act (CFAA) in the U.S.
- GDPR (EU) for handling personal data.
- Contractual obligations from clients, NDAs, and safe harbor clauses.

**Responsible Disclosure & Bug Bounties:**

- Follow the organization's vulnerability disclosure policies.
- Engage with bug bounty platforms (HackerOne, Bugcrowd) responsibly.

---

## 16. Essential Resources & Further Reading

- **OWASP Website & Cheat Sheets:** [https://owasp.org](https://owasp.org)
- **NIST Guidelines:** [https://csrc.nist.gov](https://csrc.nist.gov)
- **Pentester Academy, Offensive Security Training:** OSCP, OSCE certifications.
- **Mitre ATT&CK Framework:** For understanding adversary techniques.

---

**This cheat sheet blends methodologies, tools, code snippets, and principles to guide ethical hackers and pentesters through the entire lifecycle of a security assessment. By strictly adhering to legal, ethical, and authorized testing procedures, you can help improve security postures, protect users, and contribute positively to the cybersecurity community.**
