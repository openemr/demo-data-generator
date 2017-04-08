#!/usr/bin/env python

import click
import sys
from patient import *


@click.command()
@click.option('--count', default=1, help='Number of entities to generate')
def patient(count):
    """Generate a patient"""
    insert_patients(generate_patients(count))


def main(argv):
    if len(argv) == 0:
        print("Help menu")
        return 0

    command = argv[0]
    number = argv[1] if len(argv) > 1 else 1

    if command == "patients":
        print(insert_patients(generate_patients(int(number))))
    if command == "pharmacy":
        generate_pharmacy()
    if command == "test":
        for i in range(0, 50000):
            generate_title('Male')


if __name__ == "__main__":
    main(sys.argv[1:])

