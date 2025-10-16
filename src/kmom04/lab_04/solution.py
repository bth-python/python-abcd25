"""
This file contains the functions you shall implement to solve the lab.
Implement them one by one and check if they pass all tests.

Execute the lab using `python3 lab.py` in the terminal and review the output.
"""


def concatenate_lists(list1, list2):
    """
    Concatenate list1 and list2 and returns the result.

    Returns:
        list: list1 concatenated with list2.
    """
    return list1 + list2


def append_to_list(list1, item):
    """
    Append item to list1 and return the result. Use append().

    Returns:
        list: list1.
    """
    list1.append(item)
    return list1


def replace_third_item_in_list(list1, item):
    """
    Replace item on index in list1 and return the result.

    Returns:
        list: list1.
    """
    list1[2] = item
    return list1


def sort_list_descending(list1):
    """
    Sort list1 in descending order and return the result.

    Returns:
        list: list1.
    """
    # TODO: Write your code here
    return sorted(list1, reverse=True)


def remove_from_list(list1, item):
    """
    Remove item from list1 and return the result. Use remove()

    Returns:
        list: list1.
    """
    # TODO: Write your code here
    list1.remove(item)
    return list1


def summarize_numbers_in_list(list1):
    """
    Summarize the numbers in list1 and return the result.
    Use built-in functions, such as sum()

    Returns:
        int: sum of the numbers in list1.
    """
    # TODO: Write your code here
    return sum(list1)


def average_from_list(list1):
    """
    Count the average from the numbers in list1 and return the result.
    Use built-in functions, such as sum() and len()

    Returns:
        float: average of the numbers in list1 rounded to 1 decimal.
    """
    # TODO: Write your code here
    sum_of_list = sum(list1)
    return round(sum_of_list / len(list1), 1)


def remove_unwanted_sign(text, sign):
    """
    Use the built-in functions `split()` and `join()` to fix the string `text`,
    remove the unwanted sign `sign` with space " "
    and return the fixed string.

    Returns:
        string: a string without sign.
    """
    # TODO: Write your code here
    words = text.split(sign)
    return " ".join(words)
