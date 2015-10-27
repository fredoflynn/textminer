import re


def phone_numbers(text):
    match = re.findall(r'(\(\d{3}\) \d{3}-\d{4})', text)
    return match


def emails(text):
    match = re.findall(r'\w+(?:\.\w+)?@\w+\.\w{3}', text)
    return match
