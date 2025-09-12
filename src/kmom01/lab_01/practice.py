# password kontroll
# loopen körs än sålänge invalid password, lyckas medan användaren sriver sitt korrekt pass
# while True:
#     password = input("Enter your password: ")
#     if password == "s1h2o":
#         print("Password successfully!")
#         exit(1)
#     else:
#         print("Please enter the correct password,\n")
# print("End....")

"""Kan man få samma resultat som i koden nedan utan att använda else?
Om inte motivera varför? Om det är möjligt, förklara vilken ändring som behövs?"""

"""temperature = input("What's the temperature outside?: ")  # tar en sträng här,
if temperature <= 0:
    print("Oh no, my water bottle will freeze!")
else:
    print("Ok, then I can drink the water from my water bottle!")

    # Typeerror

temp = int(input("Whats the temperature?: "))
if temp <= 0:
    print("I am freezing...")
else:
    print("Ok i got it!") """


def m_number():
    """
    Returns the integer value 42.

    Returns:
        int: The integer value 42.
    """
    # TODO: Write your code here
    return 42


print(m_number())


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


write = input("skriv ett tal: ")
print(f"talet du har skrivit är:", float_str(write))
