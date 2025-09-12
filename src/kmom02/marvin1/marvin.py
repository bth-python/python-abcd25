"""
marvin.py
baserade text progam med olika manyval.
"""

print(r"""
                                \\\\\\\
                            \\\\\\\\\\\\
                          \\\\\\\\\\\\\\\
  -----------,-|           |C>   // )\\\\|
           ,','|          /    || ,'/////|
---------,','  |         (,    ||   /////
         ||    |          \\  ||||//''''|
         ||    |           |||||||     _|
         ||    |______      `````\____/ \
         ||    |     ,|         _/_____/ \
         ||  ,'    ,' |        /          |
         ||,'    ,'   |       |         \  |
_________|/    ,'     |      /           | |
_____________,'      ,',_____|      |    | |
             |     ,','      |      |    | |
             |   ,','    ____|_____/    /  |
             | ,','  __/ |             /   |
_____________|','   ///_/-------------/   |
              |===========,'
""")  # <-- byt ut mot din egen ASCII-bild

print("Hej! Jag heter Marvin 0.1 🤖")
print("")

while True:
    print("Meny:")
    print("1) Säga hej åt")
    print("2) Celsius till Fahrenheit")
    print("3) Poäng till betyg")
    print("4) Större/mindre/samma")
    print("5) Validera personnummer")
    print("6) Rövarspråket")
    print("q) Avsluta")
    choice = input("Ditt val: ")

    if choice == "q":
        print("Hejdå!")
        break

    elif choice == "1":
        name = input("Vad heter du? ")
        print("Tja", name, "! Kul å ha det här")

    elif choice == "2":
        celsius = float(input("Ange temperatur i Celsius: "))
        fahrenheit = round(celsius * 9 / 5 + 32, 2)
        print(f"Temperaturen i Fahrenheit blir då: {fahrenheit}")

    elif choice == "3":
        max_points = int(input("Ange maxpoäng: "))
        my_points = int(input("Ange dina poäng: "))
        percent = my_points / max_points * 100

        if percent >= 90:
            grade = "A"
        elif percent >= 80:
            grade = "B"
        elif percent >= 70:
            grade = "C"
        elif percent >= 60:
            grade = "D"
        elif percent >= 50:
            grade = "E"
        else:
            grade = "F"

        print(f"score: {grade}")

    elif choice == "4":
        print("Skriv 'ok' för att avsluta.")
        prev = None
        while True:
            value = input("Ange ett tal: ")
            if value == "ok":
                break
            try:
                num = int(value)
                if prev is None:
                    prev = num
                else:
                    if num > prev:
                        print("larger!")
                    elif num < prev:
                        print("smaller!")
                    else:
                        print("same!")
                    prev = num
            except ValueError:
                print("not a number!")

    elif choice == "5":
        person_nummer = input("Ange personnummer: ")
        person_nummer = person_nummer.replace("-", "")

        if not person_nummer.isdigit() or len(person_nummer) != 10:
            print("Not valid")
        else:
            total = 0
            for i, digit in enumerate(person_nummer):
                n = int(digit)
                if i % 2 == 0:
                    n = n * 2
                if n > 9:
                    n = n - 9
                total += n

            if total % 10 == 0:
                print("Valid")
            else:
                print("Not valid")

    elif choice == "6":
        word = input("Skriv ett ord: ")
        vowels = "AEIOUYÅÄÖaeiouyåäö"
        result = ""
        for letter in word:
            if letter in vowels or not letter.isalpha():
                result += letter
            else:
                result += letter + "o" + letter
        print(result)

    else:
        print("Felaktigt val, försök igen.")
