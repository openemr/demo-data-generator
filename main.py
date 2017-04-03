#!/usr/bin/env python

import names
import datetime
import barnum
import random
import sys
import getopt

language = 'english'
financial = ''


def generate_patients(number_of_patients=10):
    patients = []
    for x in range(0, number_of_patients):
        fname, lname = barnum.create_name()
        street, city, state, zip = generate_address()
        dob = barnum.create_birthday(1, 100)
        ss = random.randint(100000000, 999999999)
        sex = 'Male' if x % 2 == 0 else 'Female'
        pid = str(random.random())[2:]
    
        patients.append((fname, lname, street, city, state, zip, dob, ss, sex, pid))
    return patients


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


def insert_patients(patients):
    for patient in patients:
        print('INSERT INTO patient_data (fname, lname, street, city, state, postal_code, dob, ss, sex, pid) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");' % patient);


def main(argv):
    command = argv[0]
    number = argv[1] if len(argv) > 1 else 0

    if command == "patients":
        insert_patients(generate_patients(int(number)))
    if command == "pharmacy":
        generate_pharmacy()


if __name__ == "__main__":
    main(sys.argv[1:])

