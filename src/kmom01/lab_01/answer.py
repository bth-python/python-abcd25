"""
This file contains the functions you shall implement to solve the lab.
Implement them one by one and check if they pass all tests.

Execute the lab using `python3 lab.py` in the terminal and review the output.
"""


def hello():
    """
    Returns the string "Hello world".

    Returns:
        str: "Hello world".
    """
    return "Hello world"


def magic_number():
    """
    Returns the integer value 42.

    Returns:
        int: The integer value 42.
    """
    return 42


def float_str(string_number):
    """
    Returns the float number of the incoming string.

    Arguments:
        number (str): The number to cast to float.

    Returns:
        float: The float number.
    """
    return float(string_number)


def string_length(word):
    """
    Returns the length of the incoming string.

    Arguments:
        word (str): The string to use.

    Returns:
        int: The length of the string.
    """
    return len(word)


def round_pi(pi):
    """
    Returns the value of PI, rounded to three decimals.

    Arguments:
        pi (float): The value of PI to round.
    Returns:
        float: The value of PI, rounded to three decimals.
    """
    return round(pi, 3)


def concat_strings(word1, word2):
    """
    Returns a concatenated string of the incoming strings, with a space between the words.

    Arguments:
        word1 (str): The first string to use.
        word2 (str): The second string to use.

    Returns:
        str: The concatenated string.
    """
    return f"{word1} {word2}"


def char_at_position(word):
    """
    Returns the character at index 4 of the incoming string.
    Hint: String indexing starts at 0.

    Arguments:
        word (str): The string to use.

    Returns:
        str: The character at index 4 in the incoming string.
    """
    return word[4]


def lower(word):
    """
    Returns the incoming string in lowercase.
    Hint: The lower() method.

    Arguments:
        word (str): The string to use.

    Returns:
        str: The string in lowercase.
    """
    return word.lower()


def divide_string_number():
    """
    Assign the following values to variables. String '30' and integer 5.
    Convert the string to an integer and divide it by the integer.
    Round the result to the nearest integer and return it.
    Hint: int() and round()

    Returns:
        int: The rounded result of int('30') / 5.
    """
    string_number = "30"
    actual_number = 5
    result = int(string_number) / actual_number
    return round(result)


def even_or_odd(n):
    """
    Determines whether the given integer is even or odd.

    Arguments:
        n (int): The integer to check.

    Returns:
        str: "Even" if `n` is divisible by 2, otherwise "Odd".
    """
    res = ""
    if n % 2 == 0:
        res = "Even"
    else:
        res = "Odd"
    return res


def password_check(password):
    """
    Checks the length of the given password string.

    Arguments:
        password (str): The password to check.

    Returns:
        str: "Too short" if the password length is less than 5, otherwise "OK".
    """
    # Annat sätt att skriva if-satser på, om bara vill returnera ett värde
    max_len = 5
    return "Too short" if len(password) < max_len else "OK"
