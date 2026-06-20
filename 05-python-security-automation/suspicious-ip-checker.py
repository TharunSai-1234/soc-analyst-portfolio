# Suspicious IP Checker
# Fictional cybersecurity practice project

suspicious_ips = [
    "185.220.101.1",
    "45.155.205.233",
    "91.219.236.222"
]

ip_to_check = input("Enter an IP address to check: ")

if ip_to_check in suspicious_ips:
    print("ALERT: This IP address is marked as suspicious.")
    print("Recommended action: Investigate related logs and block if required.")
else:
    print("No match found in the sample suspicious IP list.")
    print("Continue normal investigation and check threat-intelligence sources.")
