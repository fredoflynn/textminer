import re


def binary(text):
    match = re.search(r'^[0-1]+$', text)
    if match:
        return match.group()


def binary_even(text):
    match = re.search(r'^[0-1]+0$', text)
    if match:
        return match.group()


def hex(text):
    match = re.search(r'^[A-F0-9]+$', text)
    if match:
        return match.group()


def word(text):
    match = re.search(r'^(?:\d*)?[a-zA-Z\-]+$', text)
    if match:
        return match.group()


def words(text, count=None):
    match = re.findall(r'\b(?:\d*)?[a-zA-Z\-]+\b', text)
    if match:
        if count is None:
            return match
        elif len(match) == count:
            return match


def phone_number(text):
    match = re.search(r'\(?\d{3}\)?[\s\.\-]?\d{3}[\-\.]?\d{4}', text)
    if match:
        return match.group()


def money(text):
    match = re.search(r'^\$\d+(?:,\d{3})?(?:,\d{3})?(,\d{3})?(?:\.\d{2})?$', text)
    if match:
        return match.group()


def zipcode(text):
    match = re.search(r'^\d{5}(?:-\d{4})?$', text)
    if match:
        return match.group()


def date(text):
    match = re.search(r'(?:\d{1,2}/)?(?:\d{1,2}/)?(?:\d{4})(?:\-\d{1,2})?(?:\-\d{1,2})?', text)
    if match and len(match.group()) > 4:
        return match.group()
