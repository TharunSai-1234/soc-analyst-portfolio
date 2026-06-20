# Failed Login Investigation Notes

## What I looked at

I reviewed a sample set of failed-login events to understand how a SOC analyst can identify possible brute-force or password-spraying activity.

The main things I checked were:

* Source IP address
* Number of failed attempts
* Number of user accounts targeted
* Login time range
* Whether there was a successful login after repeated failures

## What stood out

In this example, one source IP generated repeated failed logins against multiple accounts within a short period.

That pattern is more suspicious than a single user entering the wrong password a few times. It can indicate password spraying, especially when multiple users are targeted.

## My investigation approach

First, I would confirm whether the source IP belongs to a corporate VPN, trusted partner, or known internal system.

Then I would check:

1. Did any login succeed after the failed attempts?
2. Were privileged or admin accounts targeted?
3. Did the same IP appear in VPN, firewall, endpoint, or email logs?
4. Was there any unusual activity on the targeted accounts after the login attempts?

## What I would do next

If the activity looked malicious, I would escalate it based on severity, document the affected accounts and IP address, and recommend blocking or challenging the source IP.

I would also review whether MFA was enabled for the targeted accounts.

## Learning takeaway

This exercise helped me understand that failed-login alerts need context. A high number of failures does not always mean an attack, but repeated failures across several accounts from one source should be investigated carefully.

## Disclaimer

This is a personal learning note based on fictional or sanitized data. No employer, customer, or production information is included.
