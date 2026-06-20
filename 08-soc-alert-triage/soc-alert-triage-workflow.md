# SOC Alert Triage Workflow

## Goal

Provide a clear process for reviewing, investigating, escalating, and closing security alerts.

## Common Alert Sources

- SIEM alerts
- EDR alerts
- Firewall logs
- VPN logs
- Email security alerts
- Cloud security alerts
- Identity and authentication logs

## Step 1: Review the Alert

Check:

- Alert name
- Severity level
- Time of activity
- User account involved
- Hostname or device name
- Source IP address
- Destination IP address
- Alert description

## Step 2: Validate the Alert

Ask these questions:

- Is the activity expected or suspicious?
- Is the user known?
- Is the IP address trusted?
- Is the device managed by the organization?
- Is this a repeated alert?
- Is there related activity in other logs?

## Step 3: Investigate

1. Review SIEM logs.
2. Check endpoint activity.
3. Search the IP address in firewall and VPN logs.
4. Review user login history.
5. Check email logs if phishing is involved.
6. Search for related alerts in the same time period.
7. Map suspicious activity to MITRE ATT&CK when possible.

## Step 4: Classify the Alert

Possible outcomes:

- True Positive
- False Positive
- Benign Positive
- Needs More Investigation

## Step 5: Escalate When Needed

Escalate when:

- A privileged account is involved.
- Malware is detected.
- Multiple users are targeted.
- Sensitive data may be exposed.
- Suspicious access is confirmed.
- A cloud account may be compromised.

## Step 6: Document the Incident

Include:

- Alert summary
- Investigation steps
- Evidence collected
- Affected users or systems
- MITRE ATT&CK technique
- Containment action
- Final severity
- Closure notes

## Example Closure Note

The alert was reviewed and determined to be a false positive caused by an approved IT automation script. No malicious activity was identified. The detection rule was documented for future tuning.

## Disclaimer

This is a fictional SOC alert-triage workflow created for learning and portfolio purposes.
