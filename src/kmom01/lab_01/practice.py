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

temperature = input("What's the temperature outside?: ")  # tar en sträng här,
if temperature <= 0:
    print("Oh no, my water bottle will freeze!")
else:
    print("Ok, then I can drink the water from my water bottle!")

    # Typeerror

temp = int(input("Whats the temperature?: "))
if temp <= 0:
    print("I am freezing...")
else:
    print("Ok i got it!")
