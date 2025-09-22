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

# temp = int(input("Whats the temperature? : "))
# if temp <= 0:
#     print("I am freezing...")
# print("Ok i got it!")


# speed = 10
# mile = speed * 0.62137
# print(f"10 km is equivalent to: {mile}")


# while True:
#     name = input("whats your Name?: ")
#     if name.lower() == "ali":
#         name = name.upper()
#         print(f"Your name is correct och det är, {name}, som är ditt namn")
#         answer = input("yes/no?: ")
#         if answer.lower() == "yes" or answer.lower() == "y":
#             print("ha det så bra! ")
#         else:
#             print("inte lyckades....")
#         break
#     else:
#         print("Invalid name, det som finns registrerad stämmer ej med ditt nuvarande namn ")


#--------------------------------------------------------------------

print(r"""
    ||                   ||
    ||                   ||
    ||                   ||
    ||___________________||
    ||-------------------||
    ||                   ||
    ||                   ||
    ||                   ||
""")

while True:
    print("\nMenu")
    print("1. Your name ?")
    print("2. Change temperature celcius to fahrenheit")
    print("3. Ange dina betyg poäng")
    print("4. jämför talen")
    print("5. Skriv in din personnummer")
    print("6. Skriv nåt robber språk")
    print("q. Quit the game")

    skriv = input("Välja ett val från menyn: ")
    if skriv == "1":
        print("Hej härifrån, Marvin släpper en hälsa till dig")
    elif skriv == "2":
        celcius = float(input("Ange temperatur i celcius: "))
        fahrenheit = round((celcius * 9/5) + 32, 2)
        print(f"{celcius} motsvarar {fahrenheit}")
    elif skriv == "3":
        max_number = float(input("Ange max poäng: "))
        min_number = float(input("Ange dina poäng: "))
        percent = (min_number / max_number) * 100

        A_GRADE = 90
        B_GRADE = 80
        C_GRADE = 70
        D_GRADE = 60
        E_GRADE = 50

        if percent >= A_GRADE:
            score = "A"
        elif percent >= B_GRADE:
            score = "B"
        elif percent >= C_GRADE:
            score = "C"
        elif percent >= D_GRADE:
            score = "D"
        elif percent >= E_GRADE:
            score = "E"
        else:
            score = "F"
        print(f"Här är din betyg: {score}")
        



