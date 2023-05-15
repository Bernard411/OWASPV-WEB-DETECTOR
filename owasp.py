import subprocess

# Prompt user for target URL
target = input("Enter target URL: ")

# Set Nikto options to scan for common web application vulnerabilities, including OWASP Top 10
nikto_options = "-h " + target + " -ssl -C all -Tuning 123456bde -id 123456789 -F json -o nikto_output.json"

# Run Nikto scan and print results
nikto_output = subprocess.check_output(["nikto", nikto_options], stderr=subprocess.STDOUT, shell=True).decode()
print(nikto_output)

# Parse Nikto scan results in JSON format
import json
with open('nikto_output.json', 'r') as f:
    nikto_json = json.load(f)

# Check for OWASP Top 10 vulnerabilities in Nikto scan results
owasp_top_10_vulns = ["Injection", "Broken Authentication and Session Management", "Cross-Site Scripting (XSS)", "Broken Access Control", "Security Misconfiguration", "Insecure Cryptographic Storage", "Insufficient Transport Layer Protection", "Unvalidated and Unsanitized Input", "Insufficient Authorization", "Sensitive Data Exposure"]
for vuln in owasp_top_10_vulns:
    if vuln in nikto_json["vulnerabilities"]:
        print(vuln + " vulnerability found in target.")
