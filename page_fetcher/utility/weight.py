import math
from random import choices, randrange, uniform, sample

# https://developer.mozilla.org/en-US/docs/Glossary/Quality_values
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation/List_of_default_Accept_values

def generate_quality_values(
    values: set, priority: set = None, weightless: set = None
) -> str:
    """
    Return a string with random selected values with the respective q-value.
    Some headers field can contains multiple values separated by comma.

    Example:
        "Accept-language": "en,pt-BR,pt"
    
    This values can use "quality values" (q-values),
    to describe the order of priority for each value.
    The weight can go from 0 to 1.

    Example:
        "Accept-language": "en;q=0.9,pt-BR;q=0.8,pt;q=0.7"
    
    In this case, the server will try to feed you english first,
    brazilian portuguese second, portuguese third.
    """

    if priority is None:
        priority = set()

    if weightless is None:
        weightless = set()

    values = _add_random_weights(values, priority=priority)
    values = values.union(weightless)
    values = sample(values, len(values))

    return ",".join(values)


def _add_random_weights(values: set, priority: set) -> list:
    """
    Return a list of values with weights (ordered by weight).
    Give heightest weights to the ones inside priority.
    """
    share_size = 1.0 / len(values)

    top = 1.0
    low = 1.0 - share_size
    new = set()

    # calculate for priority values
    for p in priority:
        w = _random_weight(top, low)
        top = w
        low = low - share_size

        new.add(f"{p};q={w}")

    # calcualte for default values
    for v in values:
        w = _random_weight(top, low)
        new.add(f"{v};q={w}")

    return new


def _random_weight(top: float, low: float) -> float:
    weight = uniform(top, low)
    weight = _truncate(weight)

    if weight == 0:
        return 0.1
    return weight


def _truncate(number: float, decimal_numbers: int = 1) -> float:
    move = 10 ** decimal_numbers
    return math.trunc(move * number) / move
