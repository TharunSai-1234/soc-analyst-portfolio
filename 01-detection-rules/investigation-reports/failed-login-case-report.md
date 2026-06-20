# Failed Login Investigation Report

## Summary

I reviewed a small set of sample Windows login events after noticing repeated failed login attempts from the same IP address.

The activity came from `198.51.100.24` and targeted multiple user accounts within a few minutes.

## What I found

* 10 failed login attempts
* 5 different user accounts targeted
* Same source IP used for all failed attempts
* One successful login occurred afterward for `admin.support`

The successful login after repeated failures is the main reason this activity would need further investigation.

## Why this looked suspicious

A normal user may enter the wrong password a few times. But in this case, the same IP tried several different accounts in a short time window.

That pattern can match password spraying or brute-force behavior.

## Accounts involved

* john.smith
* finance.user
* admin.support
* hr.user
* it.helpdesk

## Investigation steps I would take

1. Check whether the source IP belongs to a company VPN, vendor, or known internal system.
2. Review login activity for `admin.support` after the successful login.
3. Check whether the account has admin privileges.
4. Search the same IP in VPN, firewall, endpoint, and email logs.
5. Check whether the targeted accounts had any password resets or suspicious activity afterward.
6. Confirm whether MFA was enabled for the affected accounts.

## Initial assessment

Based on the sample data, I would classify this as a **medium-to-high priority investigation** because multiple accounts were targeted and one account later logged in successfully.

## Recommended actions

* Investigate the successful login for `admin.support`.
* Block or challenge the source IP if it is not trusted.
* Reset passwords if compromise is suspected.
* Review MFA status for all targeted accounts.
* Add detection tuning to identify similar patterns earlier.

## MITRE ATT&CK Reference

* T1110 – Brute Force
* T1110.003 – Password Spraying

## Learning Note

This lab helped me understand why analysts should not close failed-login alerts too quickly. The number of failures matters, but the number of users targeted and whether a login later succeeds are also important.

## Disclaimer

This report uses fictional sample data for portfolio and learning purposes only.
