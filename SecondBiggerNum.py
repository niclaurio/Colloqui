from typing import List


def get_second_bigger_num(numbers: List[int]) -> int:
    """
    EX:
        get_second_bigger_num([1,5,9,2,8,3,7,4,6]) returns 8
         get_second_bigger_num([1,2,3,4,5,6,7,8,9]) returns 8
    :param numbers:
    :return:
    """
    if len(numbers) < 2:
        raise ValueError("the list of numbers must contain minimum 2 numbrs")
    try:
        assert all(isinstance(number, int) for number in numbers)
    except AssertionError:
        raise TypeError("you did not insert a list of numbers ")
    numbers.sort(reverse=True)
    return numbers[1]