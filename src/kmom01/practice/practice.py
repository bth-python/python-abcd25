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

temp = int(input("Whats the temperature? : "))
if temp <= 0:
    print("I am freezing...")
print("Ok i got it!")


speed = 10
mile = speed * 0.62137
print(f"10 km is equivalent to: {mile}")


while True:
    name = input("whats your Name?: ")
    if name.lower() == "ali":
        name = name.upper()
        print(f"Your name is correct och det är, {name}, som är ditt namn")
        answer = input("yes/no?: ")
        if answer.lower() == "yes" or answer.lower() == "y":
            print("ha det så bra! ")
        else:
            print("inte lyckades....")
        break
    else:
        print("Invalid name, det som finns registrerad stämmer ej med ditt nuvarande namn ")
