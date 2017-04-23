import random
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
