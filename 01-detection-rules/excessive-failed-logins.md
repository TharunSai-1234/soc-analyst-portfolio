# Detection Use Case: Excessive Failed Logins

## Goal

Detect possible brute-force or password-spraying attacks.

## What Are We Looking For?

Someone trying many wrong passwords to get into user accounts.

## Data Sources

- Windows Security Logs
- VPN Logs
- Microsoft Defender Logs
- Identity Provider Login Logs

## Detection Logic

Create an alert when:

- One IP address has more than 10 failed logins
- It targets 5 or more users
- All activity happens within 10 minutes

## MITRE ATT&CK Mapping

- T1110 - Brute Force
- T1110.003 - Password Spraying

## Sample Splunk Query

```spl
index=windows EventCode=4625
| stats count dc(user) AS targeted_users values(user) AS users by src_ip
| where count >= 10 AND targeted_users >= 5
```

## Investigation Steps

1. Check whether the IP address is internal or external.
2. Check whether any login attempt was successful.
3. Check whether privileged accounts were targeted.
4. Search the IP address in VPN, firewall, endpoint, and email logs.
5. Escalate the alert when activity looks suspicious.

## Possible False Positives

- User forgot their password.
- Service account has an old password.
- VPN login issue.
- Approved vulnerability scanner activity.

## Recommended Response

- Block the suspicious IP address when required.
- Reset affected user passwords.
- Confirm MFA is enabled.
- Document findings in the incident ticket.

## Disclaimer

This is a fictional detection example created only for learning and portfolio purposes.
