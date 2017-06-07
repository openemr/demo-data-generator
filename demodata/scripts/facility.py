"""Generate facility data"""

import barnum
from demodata.util import *

__copyright__ = "Copyright (C) 2017 Robert Down"
__author__ = "Robert Down <robertdown@live.com>"
__license__ = "GNU GPL3"


def generate_facility(count=1):
    random.seed()
    facilities = []
    for x in range(0, count):
        street, city, state, postal_code = generate_address()
        name = barnum.create_company_name()
        billing = random_truth(0.8)
        assignment = 0
        if billing:
            assignment = random_truth(0.8)

        # TODO domain_id, pos_code, facility_id, website
        facility = {
            'name': name,
            'street': street,
            'city': city,
            'state': state,
            'country_code': 'US',
            'postal_code': postal_code,
            'phone': barnum.create_phone(postal_code),
            'fax': barnum.create_phone(postal_code),
            'tax_id_type': "EI",
            'federal_ein': random.randint(10000000000, 99999999999),
            'facility_npi': random.randint(1000000000, 9999999999),
            'website': '',
            'email': barnum.create_email(name=name),
            'billing_location': billing,
            'accepts_assignment': assignment,
            'service_location': 1,
            'color': generate_hex_color(),
            'primary_business_entity': 1,
            'pos_code': '21',
            'attn': '',
            'domain_identifier': '',
            'facility_id': '%s-%s' % (name, str(random.randint(10000, 99999)))
        }

        facilities.append(facility)

    return facilities
