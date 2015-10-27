import re


def words(text):
    new = re.findall(r'\b(?:\d*\-?)?[A-Za-z]+\b', text)
    if new:
        return new


def phone_numbers(text):
    number_dict = {}
    match = re.search(r'\(?(\d{3})\)?[\.\s\-]?(\d{3})[\.\-]?(\d{4})', text)
    if match:
        number_dict['area_code'] = match.groups()[0]
        number_dict['number'] = match.groups()[1] + '-' + match.groups()[2]
        return number_dict


def money(text):
    money_dict = {}
    match = re.search(r'^(\$)(\d+(?:,\d{3})?(?:,\d{3})?(,\d{3})?(?:\.\d{2})?$)', text)
    if match:
        money_dict['currency'] = match.groups()[0]
        amt = re.sub(r',', "", match.groups()[1])
        money_dict['amount'] = float(amt)
        return money_dict


def zip(text):
    zip_dict = {}
    match = re.search(r'^(\d{5})(?:-(\d{4}))?$', text)
    if match:
        zip_dict['zip'] = match.groups()[0]
        zip_dict['plus4'] = match.groups()[1]
        return zip_dict


def date(text):
    date_dict = {}
    match = re.search(r'(?:(\d{1,2})/)?(?:(\d{1,2})/)?(?:(\d{4}))(?:\-(\d{1,2}))?(?:\-(\d{1,2}))?', text)
    if match:
        if match.groups()[0] is None and match.groups()[4] is None:
            return None
        elif match.groups()[0] is None:
            date_dict['month'] = int(match.groups()[3])
            date_dict['day'] = int(match.groups()[4])
            date_dict['year'] = int(match.groups()[2])
            return date_dict
        elif match.groups()[4] is None:
            date_dict['month'] = int(match.groups()[0])
            date_dict['day'] = int(match.groups()[1])
            date_dict['year'] = int(match.groups()[2])
            return date_dict
