# Incident Response Playbook: Phishing Email

## Goal

Provide a simple SOC process for investigating and responding to phishing emails.

## Alert Sources

- Email security gateway
- Microsoft Defender for Office 365
- User-reported suspicious emails
- SIEM alerts

## Initial Triage

1. Check sender email address.
2. Check subject line and email body.
3. Review email headers.
4. Check links and attachments.
5. Identify all users who received the email.

## Investigation Steps

1. Check whether any user clicked the suspicious link.
2. Check whether any attachment was downloaded or opened.
3. Search the sender domain, URL, and IP address in threat-intelligence tools.
4. Check endpoint logs for suspicious activity.
5. Check whether user credentials were entered on a fake website.

## Containment Actions

- Block the sender domain.
- Block malicious URLs.
- Quarantine similar emails.
- Reset passwords if credentials may be compromised.
- Isolate affected endpoint if malware execution is suspected.

## MITRE ATT&CK Mapping

- T1566 - Phishing
- T1566.001 - Spearphishing Attachment
- T1566.002 - Spearphishing Link

## Documentation Required

- Affected users
- Sender details
- Malicious URLs or attachments
- Investigation timeline
- Containment actions taken
- Final incident severity

## Disclaimer

This is a fictional playbook created for learning and portfolio purposes.
