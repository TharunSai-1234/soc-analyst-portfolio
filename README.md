# SOC Analyst Portfolio

> A hands-on cybersecurity portfolio focused on SOC operations, detection engineering, incident response, threat hunting, cloud security monitoring, and security automation.

## Purpose

This repository contains self-directed cybersecurity lab work and sanitized examples created for learning and portfolio purposes.

No employer, customer, confidential, personal, or production data is included.

## Skills Demonstrated

- SIEM use-case development and alert tuning
- Threat hunting using MITRE ATT&CK
- Incident response workflows and playbooks
- Phishing and email-threat analysis
- AWS CloudTrail and GuardDuty monitoring concepts
- Detection engineering and false-positive reduction
- Python-based security automation

## Portfolio Sections

| Folder | What It Shows |
|---|---|
| `01-detection-rules` | SIEM detection use cases and tuning ideas |
| `02-incident-response-playbooks` | SOC incident response procedures |
| `03-threat-hunting` | Threat-hunting hypotheses and investigation workflows |
| `04-cloud-security-monitoring` | AWS and cloud security detection examples |
| `05-python-security-automation` | Small Python scripts for SOC tasks |

## Tools and Frameworks

Splunk · QRadar · ArcSight · CrowdStrike Falcon · Microsoft Defender · AWS GuardDuty · AWS CloudTrail · Qualys · Nessus · MITRE ATT&CK · Python

## Disclaimer

All examples in this repository use fictional or sanitized lab data. They do not represent work performed for any employer or client.
## Featured Projects

### 1. SIEM Detection Rule
[Excessive Failed Logins Detection Rule](01-detection-rules/excessive-failed-logins.md)  
Detects possible brute-force and password-spraying activity using failed-login patterns.

### 2. Incident Response Playbook
[Phishing Incident Response Playbook](02-incident-response-playbooks/phishing-incident-response.md)  
Shows a SOC workflow for investigating, containing, and documenting phishing incidents.

### 3. Threat Hunting Use Case
[Suspicious PowerShell Threat Hunt](03-threat-hunting/suspicious-powershell-hunt.md)  
Looks for suspicious PowerShell behavior such as encoded commands, downloads, and hidden execution.

### 4. AWS Cloud Security Monitoring
[AWS CloudTrail and GuardDuty Alert Use Case](04-cloud-security-monitoring/aws-cloudtrail-guardduty-alert.md)  
Covers suspicious IAM changes, access-key creation, privilege escalation, and CloudTrail monitoring.

### 5. Python Security Automation
[Suspicious IP Checker Script](05-python-security-automation/suspicious-ip-checker.py)  
A simple Python practice script that checks an IP address against a sample suspicious-IP list.
