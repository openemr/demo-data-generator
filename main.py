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
		street = barnum.create_street()
		zip, city, state = barnum.create_city_state_zip()
		dob = barnum.create_birthday(1, 100)
		ss = random.randint(100000000, 999999999)
		sex = 'Male' if x % 2 == 0 else 'Female'
		pid = str(random.random())[2:]
	
		patients.append((fname, lname, street, city, state, zip, dob, ss, sex, pid))
	return patients

def insert_patients(patients):
	for patient in patients:
		print('INSERT INTO patient_data (fname, lname, street, city, state, postal_code, dob, ss, sex, pid) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");' % patient);

def main(argv):
	command = argv[0]
	number = argv[1]

	if command == "patients":
		insert_patients(generate_patients(int(number)))


if __name__ == "__main__":
	main(sys.argv[1:])

