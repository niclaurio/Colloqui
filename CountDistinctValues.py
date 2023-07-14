from typing import Dict, Iterable


def count_values(vals: Iterable) -> Dict[str, int]:
    """
    it calculates how many times each element is repeted
    """
    distinct_vals = set(vals)
    return {str(val):vals.count(val) for val in distinct_vals}
