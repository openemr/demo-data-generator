"""Generate patient data"""

import barnum
from demodata.util import *

__copyright__ = "Copyright (C) 2017 Robert Down"
__author__ = "Robert Down <robertdown@live.com>"
__license__ = "GNU GPL3"


def generate_patients(count=1):
    random.seed()
    patients = []
    for x in range(0, count):
        sex = 'Male' if random.randint(0, 1) % 2 else 'Female'
        fname, lname = barnum.create_name(gender=sex)
        mname = barnum.create_name(False, sex) if random_truth(0.27) == 1 else ''
        street, city, state, postal_code = generate_address()
        dob = barnum.create_birthday(1, 100)

        patient = {
            'title': generate_title(sex),
            'language': '',
            'financial': '',
            'fname': fname,
            'lname': lname,
            'mname': mname,
            'DOB': dob.strftime("%Y-%m-%d"),
            'street': street,
            'postal_code': postal_code,
            'city': city,
            'state': state,
            'country_code': 'US',
            'drivers_license': random_drivers_license(lname[0], int(dob.strftime("%y"))),
            'ss': random.randint(100000000, 999999999),
            'occupation': barnum.create_job_title(),
            'phone_home': barnum.create_phone(postal_code),
            'phone_biz': barnum.create_phone(postal_code),
            'phone_contact': barnum.create_phone(postal_code),
            'phone_cell': barnum.create_phone(postal_code),
            'pharmacy_id': 1,
            'status': '',
            'contact_relationship': '',
            'date': barnum.create_date(past=True).strftime("%Y-%m-%d"),
            'sex': sex,
            'referrer': '',
            'referrerID': '',
            'providerID': 0,
            'ref_providerID': 0,
            'email': barnum.create_email(name=(fname, lname)),
            'email_direct': '',
            'ethnoracial': '',
            'race': '',
            'ethnicity': '',
            'religion': '',
            'interpretter': '',
            'migrantseasonal': '',
            'family_size': random.randint(1, 8),
            'monthly_income': '',
            'billing_note': '',
            'homeless': '',
            'financial_review': barnum.create_date(past=True).strftime("%Y-%m-%d"),
            'pubpid': '',
            'pid': str(random.randint(1, 99999999999)),
            'hipaa_mail': 'yes' if random_truth(0.90) == 1 else 'no',
            'hipaa_voice': 'yes' if random_truth(0.75) == 1 else 'no',
            'hipaa_notice': 'yes' if random_truth(0.93) == 1 else 'no',
            'hipaa_message': 'yes' if random_truth(0.90) == 1 else 'no',
            'hipaa_allowsms': 'yes' if random_truth(0.50) == 1 else 'no',
            'hipaa_allowemail': 'yes' if random_truth(0.70) == 1 else 'no',
        }
        patients.append(patient)

    return patients


def random_drivers_license(initial_letter=None, year=None):
    if not initial_letter:
        letters = (
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z')
        initial_letter = random.choice(letters)
    if not year:
        year = random.randint(10, 99)

    triplicate = [random.randint(000, 999), random.randint(100, 999), random.randint(100, 999)]

    return "%s%i-%i-%i-%i" % (initial_letter, triplicate[0], triplicate[1], year, triplicate[2])


def generate_title(gender=None):
    """
    Randomly select a title based on given gender

    Example: "Mr."
    """
    random.seed()
    if gender is None:
        return ''
    if gender == 'Male':
        titles = {'': 47, 'Mr.': 49, 'Dr.': 3}
    if gender == 'Female':
        titles = {'': 47, 'Mrs.': 30, 'Ms.': 23}

    weighted_titles = []

    for t, w in titles.items():
        weighted_titles.extend(repeat(t, w))

    r = random.randint(0, 99)

    return weighted_titles[r - 1 if r > 0 else 0]


def generate_pharmacy():
    name = barnum.create_company_name()
    street, city, state, zip = generate_address()
    email = barnum.create_email()
    phone = barnum.create_phone(zip)
    fax = barnum.create_phone(zip)
    return name, street, city, state, zip, email, phone, fax
