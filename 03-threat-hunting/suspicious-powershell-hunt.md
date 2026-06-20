# Threat Hunt: Suspicious PowerShell Activity

## Goal

Find possible malicious or unusual PowerShell commands running on user systems.

## Why PowerShell?

Attackers may use PowerShell to download files, run hidden commands, or steal information.

## Data Sources

- Windows PowerShell Logs
- Microsoft Defender for Endpoint
- Sysmon Logs
- SIEM Alerts

## Hunt Hypothesis

An attacker may use encoded or hidden PowerShell commands to avoid detection.

## What To Look For

- Encoded commands
- Hidden PowerShell windows
- Download commands
- PowerShell started from Microsoft Office
- PowerShell started by unusual parent processes

## Example Splunk Search

```spl
index=windows powershell
(CommandLine="*EncodedCommand*" OR CommandLine="*DownloadString*" OR CommandLine="*Hidden*")
| table _time host user ParentImage CommandLine
```

## MITRE ATT&CK Mapping

- T1059.001 - PowerShell
- T1027 - Obfuscated Files or Information
- T1105 - Ingress Tool Transfer

## Investigation Steps

1. Check the user and device involved.
2. Review the full PowerShell command.
3. Check which process started PowerShell.
4. Look for downloaded files or suspicious URLs.
5. Check endpoint alerts for malware activity.
6. Escalate if the command is suspicious or malicious.

## Possible False Positives

- IT automation scripts
- Approved admin scripts
- Software deployment tools
- Security scanning tools

## Disclaimer

This is a fictional threat-hunting example created for learning and portfolio purposes.
