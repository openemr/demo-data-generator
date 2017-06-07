import random
import barnum
from itertools import repeat


def random_truth(weight=None):
    """Randomly select true or false
    
    Use weight-based formula to randomly select true or false
    
    Keyword arguments:
        weight -- the weight to apply to True (default is 0.50)
    """
    random.seed()
    if not weight:
        weight = 500
    else:
        weight = int(weight * 1000)

    p = []

    p.extend(repeat(0, 1000 - weight))
    p.extend(repeat(1, weight))

    return p[random.randint(0, 999)]


def generate_hex_color():
    random.seed()
    opts = "A,B,C,D,E,F,0,1,2,3,4,5,6,7,8,9"
    opts = opts.split(",")
    color = []
    for x in range(0, 6):
        n = random.randrange(len(opts))
        color.append(opts[n])

    result = "#" + "".join(color)
    return result


def generate_sql(table_name, object):
    sql_string = ""
    for row in object:
        columns = ", ".join(row.keys())
        values_list = []
        for v in row.values():
            value = '"' + str(v) + '"'
            values_list.append(value)

        values = ", ".join(values_list)
        line = "INSERT INTO `%s` (%s) VALUES (%s);\n" % (table_name, columns, values)
        sql_string = sql_string + line
    return sql_string


def generate_address():
    street = barnum.create_street()
    zip, city, state = barnum.create_city_state_zip()
    return street, city, state, zip
