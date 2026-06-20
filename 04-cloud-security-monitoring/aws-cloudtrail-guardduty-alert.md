# AWS Cloud Security Monitoring: Suspicious IAM Activity

## Goal

Detect suspicious activity involving AWS IAM users, roles, or access keys.

## Why This Matters

Attackers may try to create new users, change permissions, disable logging, or use stolen AWS access keys.

## Data Sources

- AWS CloudTrail
- AWS GuardDuty
- AWS IAM Logs
- AWS CloudWatch Logs
- SIEM Platform

## Suspicious Activities To Monitor

- Multiple failed AWS console login attempts
- IAM user creation
- New access key creation
- Privilege escalation attempts
- IAM policy changes
- CloudTrail logging disabled
- Login from unusual country or IP address

## Example CloudTrail Events

- CreateUser
- CreateAccessKey
- AttachUserPolicy
- PutUserPolicy
- DeleteTrail
- StopLogging
- ConsoleLogin

## Detection Logic

Create a high-severity alert when:

- A new IAM user is created
- An access key is created for that user
- Administrator permissions are assigned
- All actions happen within a short time period

## MITRE ATT&CK Mapping

- T1078 - Valid Accounts
- T1098 - Account Manipulation
- T1531 - Account Access Removal
- T1562.008 - Disable or Modify Cloud Logs

## Investigation Steps

1. Identify the IAM user or role that performed the activity.
2. Check whether the source IP address is approved.
3. Review CloudTrail events before and after the suspicious action.
4. Check whether new access keys were created.
5. Review permission changes.
6. Check GuardDuty findings for related alerts.
7. Escalate immediately if administrator access was granted.

## Recommended Response

- Disable suspicious access keys.
- Revoke unnecessary IAM permissions.
- Rotate compromised credentials.
- Enable MFA for affected accounts.
- Confirm CloudTrail logging is active.
- Document all actions in the incident ticket.

## Disclaimer

This is a fictional AWS security monitoring example created for learning and portfolio purposes.
