#!/usr/bin/env python

import click
import sys
from patient import *

language = 'english'
financial = ''


@click.command()
@click.option('--count', default=1, help='Number of entities to generate')
def patient(count):
    """Generate a patient"""
    insert_patients(generate_patients(count))


def insert_patients(patients):
    pass


def main(argv):
    if len(argv) == 0:
        print("Help menu")
        return 0

    command = argv[0]
    number = argv[1] if len(argv) > 1 else 1

    if command == "patients":
        # insert_patients(generate_patients(int(number)))
        patient_list = generate_patients(number)
        print(patient_list[0]["drivers_license"], patient_list[0]["lname"], patient_list[0]['DOB'])
    if command == "pharmacy":
        generate_pharmacy()
    if command == "test":
        print(random_drivers_license())


if __name__ == "__main__":
    main(sys.argv[1:])

