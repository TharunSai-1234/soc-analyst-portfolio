# Phishing Email Header Analysis

## Goal

Analyze a suspicious email and identify signs of phishing.

## What I Check

- Sender email address
- Reply-To address
- Email subject
- SPF result
- DKIM result
- DMARC result
- Received headers
- Suspicious links
- Attachments
- Sender IP address

## Example Suspicious Indicators

- Sender domain does not match the company name
- Reply-To address is different from sender address
- SPF, DKIM, or DMARC validation fails
- Email contains urgent language such as "Verify now" or "Your account will be disabled"
- Link points to an unfamiliar domain
- Attachment contains `.exe`, `.zip`, `.html`, or macro-enabled files

## Investigation Steps

1. Review the sender and Reply-To email addresses.
2. Check the email header for SPF, DKIM, and DMARC results.
3. Extract links without clicking them.
4. Check domains and URLs using threat-intelligence tools.
5. Identify all users who received the email.
6. Check whether any user clicked the link or opened the attachment.
7. Search endpoint and proxy logs for related activity.
8. Escalate if credentials, malware, or malicious links are involved.

## Example Email Header Fields

```text
From: support@secure-microsoft-login.com
Reply-To: verify.account@gmail.com
Subject: Urgent: Your Microsoft Account Will Be Disabled
SPF: Fail
DKIM: Fail
DMARC: Fail
```

## Possible Response Actions

- Quarantine the email
- Block sender domain
- Block malicious URL
- Notify affected users
- Reset passwords if credentials were entered
- Isolate affected endpoint if malware execution is suspected

## MITRE ATT&CK Mapping

- T1566 - Phishing
- T1566.001 - Spearphishing Attachment
- T1566.002 - Spearphishing Link

## Disclaimer

This is a fictional phishing-analysis example created only for learning and portfolio purposes.
