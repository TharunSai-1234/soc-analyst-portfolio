# Failed Login Detection Case Study

This folder contains a small SOC investigation case study based on repeated failed-login activity.

I used this example to practice how I would review an authentication alert, identify suspicious patterns, and decide whether the activity should be escalated.

## What is included

* `excessive-failed-logins.md` — detection logic for repeated failed logins across multiple users
* `failed-login-case-report.md` — investigation notes and recommended next actions
* `sample-data/` — fictional sample events used for learning

## Scenario

The case focuses on one source IP generating multiple failed login attempts against different user accounts within a short period.

The main question is whether the activity is normal user behavior, a service-account issue, or possible password spraying.

## What I would validate

* Whether the source IP is trusted
* Whether any login succeeded after repeated failures
* Whether privileged accounts were targeted
* Whether the same IP appears in VPN, firewall, endpoint, or email logs
* Whether MFA was enabled for affected accounts

## Takeaway

Failed-login alerts need context. A few failures from one user may be normal, but repeated attempts against several accounts from one source need closer investigation.

> All content in this folder uses fictional or sanitized learning data only.
