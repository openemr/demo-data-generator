import random
from itertools import repeat


def random_truth(weight=None):
    random.seed()
    if not weight:
        weight = 500
    else:
        weight = int(weight * 1000)

    possibilities = []

    possibilities.extend(repeat(0, 1000 - weight))
    possibilities.extend(repeat(1, weight))

    return possibilities[random.randint(0, 999)]
