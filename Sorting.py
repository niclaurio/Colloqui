from typing import List


def sorting(vals: List, reverse=False):
    """
    Ex:
        sorting([1,9,5,2,8,3,7,4,6]) returns  [1,2,3,4,5,6,7,8,9]
        sorting([1,9,5,2,8,3,7,4,6], reverse=True) returns  [9,8,7,6,5,4,3,2,1]
    """
    if not vals:
        raise ValueError("it is not possible to sort an empty list")
    if not has_only_one_datatype(vals):
        raise TypeError("it is not possible to sort a list whose elements have different type")
    for i in range(len(vals)):
        for j in range(i+1, len(vals)):
            if vals[j] < vals[i]:
                aux_ = vals[i]
                vals[i] = vals[j]
                vals[j] = aux_
    if reverse:
        return vals[::-1]
    return vals


def has_only_one_datatype(vals: List) -> bool:
    '''
    EX:
        [1,2,3,4] returns True
        ['a', 1, 'b', {'a':1}] returns False
    '''
    return len({type(el) for el in vals}) == 1
