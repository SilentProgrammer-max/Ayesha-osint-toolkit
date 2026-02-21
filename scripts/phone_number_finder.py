# scripts/phone_number_finder.py
import re

def find_phone_numbers(text):
    pattern = r"\+?\d[\d -]{8,}\d"
    return re.findall(pattern, text)

if __name__ == "__main__":
    sample = "Call us at +1-800-123-4567 or 0345-6789012"
    numbers = find_phone_numbers(sample)
    print("Found Phone Numbers:", numbers)
