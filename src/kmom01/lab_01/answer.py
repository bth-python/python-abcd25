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
    # TODO: Write your code here
    return "Hello world"


print(hello())


def magic_number():
    """
    Returns the integer value 42.

    Returns:
        int: The integer value 42.
    """
    # TODO: Write your code here
    nbr = 42
    return nbr


print(magic_number())


def float_str(string_number):
    """
    Returns the float number of the incoming string.

    Arguments:
        number (str): The number to cast to float.

    Returns:
        float: The float number.
    """
    # TODO: Write your code here
    return float(string_number)


print(float_str("3.235235"))


def string_length(word):
    """
    Returns the length of the incoming string.

    Arguments:
        word (str): The string to use.

    Returns:
        int: The length of the string.
    """
    # TODO: Write your code here
    return len(word)


print(string_length("Hussain"))


def round_pi(pi):
    """
    Returns the value of PI, rounded to three decimals.

    Arguments:
        pi (float): The value of PI to round.
    Returns:
        float: The value of PI, rounded to three decimals.
    """
    # TODO: Write your code here
    return round(pi, 3)


print(round_pi(3.1421356))


def concat_strings(word1, word2):
    """
    Returns a concatenated string of the incoming strings, with a space between the words.

    Arguments:
        word1 (str): The first string to use.
        word2 (str): The second string to use.

    Returns:
        str: The concatenated string.
    """
    # TODO: Write your code here
    return word1 + " " + word2


print(concat_strings("hej", "Hur är läget"))
print(concat_strings("fine", "Tackar"))


def char_at_position(word):
    """
    Returns the character at index 4 of the incoming string.
    Hint: String indexing starts at 0.

    Arguments:
        word (str): The string to use.

    Returns:
        str: The character at index 4 in the incoming string.
    """
    # TODO: Write your code here
    return word[4]


print(char_at_position("Indexering"))
print(char_at_position("index"))


def divide_string_number():
    """
    Assign the following values to variables. String '30' and integer 5.
    Convert the string to an integer and divide it by the integer.
    Round the result to the nearest integer and return it.
    Hint: int() and round()

    Returns:
        int: The rounded result of int('30') / 5.
    """
    # TODO: Write your code here

    str_nbr = "30"
    nbr = 5
    result = int(str_nbr) / nbr
    return round(result)


print(divide_string_number())


def even_or_odd(n):
    """
    Determines whether the given integer is even or odd.

    Arguments:
        n (int): The integer to check.

    Returns:
        str: "Even" if `n` is divisible by 2, otherwise "Odd".
    """
    # TODO: Write your code here
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


print(even_or_odd(33))
print(even_or_odd(24))


def password_check(password):
    """
    Checks the length of the given password string.

    Arguments:
        password (str): The password to check.

    Returns:
        str: "Too short" if the password length is less than 5, otherwise "OK".
    """
    # TODO: Write your code here
    password_len = 5
    if len(password) < password_len:
        return "low password"
    else:
        return "OK"


print(password_check("3fdw"))
