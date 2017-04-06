import barnum
from util import *


def generate_patients(count=1):
    patients = []
    for x in range(0, count):
        gender = 'Male' if random.randint(0, 1) % 2 else 'Female'
        fname, lname = barnum.create_name(gender=gender)
        mname = barnum.create_name(False, gender) if random_truth(0.27) == 1 else ''
        street, city, state, postal_code = generate_address()
        dob = barnum.create_birthday(1, 100)

        patient = {
            'title': generate_title(gender),
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
            'pharmacy_id': '',
            'status': '',
            'contact_relationship': '',
            'date': '',
            'sex': gender,
            'referrer': '',
            'referrerID': '',
            'providerID': '',
            'ref_providerID': '',
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
            'financial_review': '',
            'pubpid': '',
            'pid': str(random.random())[2:],
            'hippa_mail': 'yes' if random_truth(0.90) == 1 else 'no',
            'hippa_voice': 'yes' if random_truth(0.75) == 1 else 'no',
            'hippa_notice': 'yes' if random_truth(0.93) == 1 else 'no',
            'hippa_message': 'yes' if random_truth(0.90) == 1 else 'no',
            'hippa_allowsms': 'yes' if random_truth(0.50) == 1 else 'no',
            'hippa_allowemail': 'yes' if random_truth(0.70) == 1 else 'no',
        }
        patients.append(patient)

    return patients


def random_drivers_license(initial_letter=None, year=None):
    if not initial_letter:
        letters = (
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V',
            'W', 'X', 'Y', 'Z')
        initial_letter = random.choice(letters)
    if not year:
        year = random.randint(10, 99)

    triplicate = [random.randint(000, 999), random.randint(100, 999), random.randint(100, 999)]

    return "%s%i-%i-%i-%i" % (initial_letter, triplicate[0], triplicate[1], year, triplicate[2])


def insert_patients(patients):
    pass


def generate_title(gender=None):
    """
    Randomly select a title based on given gender

    Example: "Mr."
    """
    if gender is None:
        return ''
    if gender == 'Male':
        titles = {'': 47, 'Mr.': 49, 'Dr.': 3}
    if gender == 'Female':
        titles = {'': 47, 'Mrs.': 30, 'Ms.': 23}

    weighted_titles = []

    for t, w in titles.items():
        weighted_titles.extend(repeat(t, w))

    return weighted_titles[random.randint(0, 99)]


def generate_address():
    street = barnum.create_street()
    zip, city, state = barnum.create_city_state_zip()
    return street, city, state, zip


def generate_pharmacy():
    name = barnum.create_company_name()
    street, city, state, zip = generate_address()
    email = barnum.create_email()
    phone = barnum.create_phone(zip)
    fax = barnum.create_phone(zip)
    return name, street, city, state, zip, email, phone, fax
