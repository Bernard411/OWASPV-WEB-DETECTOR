# OWASPV-WEB-DETECTOR

The code is a Python script that uses the Nikto tool to scan a target URL for common web application vulnerabilities,
including those listed in the OWASP Top 10. The script prompts the user to input a target URL, sets the Nikto options for the scan,
runs the scan, and prints the results. The script then parses the Nikto scan results in JSON format, checks for OWASP Top 10 vulnerabilities,
and writes the results to a separate JSON file.

To use the script, the user should have Nikto installed on their system. 
They can then run the script and input the target URL when prompted.
The script will output the Nikto scan results to the console and write the OWASP scan results to a file named "owasp_scan_results.json" in the current directory.

Note: This script is provided as an example and should be used with caution.
It is recommended that users have a good understanding of web application security and take appropriate measures to ensure the safety of their systems.


