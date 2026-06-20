# SOC Security Dashboard Design

## Goal

Create a SOC dashboard that helps analysts quickly understand security activity, active threats, and high-risk systems.

## Dashboard Purpose

The dashboard should help the SOC team answer:

- What alerts are happening right now?
- Which alerts are high severity?
- Which users or systems are most targeted?
- Are there suspicious login attempts?
- Are phishing alerts increasing?
- Are there cloud-security incidents?
- Which detection rules create too many false positives?

## Main Dashboard Panels

### 1. Alerts by Severity

Show alerts grouped by:

- Critical
- High
- Medium
- Low

This helps analysts focus on the most important alerts first.

### 2. Top Alert Types

Show the most common alert categories, such as:

- Failed logins
- Malware detections
- Phishing emails
- Suspicious PowerShell
- IAM policy changes
- VPN alerts

### 3. Top Source IP Addresses

Show IP addresses generating the most alerts.

Useful for identifying:

- Brute-force attacks
- Password spraying
- Malicious scanning
- Suspicious external activity

### 4. Most Targeted Users

Show users who receive the most alerts.

Pay extra attention to:

- Admin accounts
- Finance users
- Executives
- Service accounts

### 5. Failed Login Trend

Show failed-login activity over time.

A sudden spike may indicate brute-force or password-spraying activity.

### 6. Endpoint Alerts

Show endpoint activity such as:

- Malware detections
- Suspicious processes
- PowerShell activity
- USB device alerts
- EDR detections

### 7. Cloud Security Alerts

Show alerts from:

- AWS GuardDuty
- AWS CloudTrail
- Azure security logs
- IAM activity
- Unusual cloud logins

### 8. Phishing Alerts

Show:

- Reported phishing emails
- Blocked sender domains
- Suspicious URLs
- Users who clicked malicious links
- Attachment-based threats

## Example SOC Metrics

- Total alerts today
- Critical alerts open
- Mean time to acknowledge
- Mean time to resolve
- Alerts by source
- Top affected users
- Top affected endpoints
- False-positive rate
- Detection rules needing tuning

## Investigation Workflow

1. Identify high-severity alerts.
2. Review affected users, devices, and IP addresses.
3. Check related SIEM, EDR, cloud, and email logs.
4. Determine whether the alert is a true positive or false positive.
5. Escalate confirmed incidents.
6. Tune noisy detection rules when needed.

## Recommended Tools

- Splunk
- QRadar
- ArcSight
- Microsoft Sentinel
- CrowdStrike Falcon
- Microsoft Defender for Endpoint
- AWS GuardDuty
- AWS CloudTrail

## Disclaimer

This is a fictional SIEM dashboard design created for learning and portfolio purposes.
