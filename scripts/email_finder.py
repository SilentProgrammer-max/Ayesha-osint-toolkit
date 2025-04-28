# This script searches for email addresses associated with a domain.
# scripts/email_finder.py
import re

def find_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

if __name__ == "__main__":
    sample = "Contact us at support@example.com or admin@example.org"
    emails = find_emails(sample)
    print("Found Emails:", emails)
