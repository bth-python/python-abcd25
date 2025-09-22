def greet():
    print("Hej Ali heter jag, å Robot hälsar dig tillbaka 🤚")


def celsius_to_fahrenheit():
    celcius = float(input("Skriv temperaturen i Celcius:"))
    fahrenheit = round((celcius * 9 / 5) + 32, 2)
    print(f"{celcius} °C Celcius motsvarar {fahrenheit: 2} °F Fahrenheit")


def points_to_grade():
    max_poang = float(input("Ange Max poang: "))
    din_poang = float(input("Ange dina poang: "))
    procent = (din_poang / max_poang) * 100

    GRADE_A = 90
    GRADE_B = 80
    GRADE_C = 70
    GRADE_D = 60
    GRADE_E = 50

    if procent >= GRADE_A:
        betyg = "A"
    elif procent >= GRADE_B:
        betyg = "B"
    elif procent >= GRADE_C:
        betyg = "C"
    elif procent >= GRADE_D:
        betyg = "D"
    elif procent >= GRADE_E:
        betyg = "E"
    else:
        betyg = "F"
    print(f"Betyg: {betyg}")


def compare_number():
    old_value = None
    while True:
        value = input("Skriv ett tal eller (skriv done för att avsluta): ")
        if value == "done":
            break
        try:
            tal = float(value)
            if old_value is None:
                old_value = tal
                continue
            if tal > old_value:
                print(f"{tal} is larger than {old_value}")
            elif tal < old_value:
                print(f"{tal} is smaller than {old_value}")
            else:
                print("same")
            old_value = tal
        except ValueError:
            print("Not a number")


def validate_ssn():
    personnummer = input("Skriv in personnummer: ").replace("-", "")
    LENGHT_PERSONNUMMER = 10
    if not personnummer.isdigit() or len(personnummer) != LENGHT_PERSONNUMMER:
        print("Not a valid personnummer")
        return

    total = 0
    for i, digit in enumerate(personnummer):
        tal_n = int(digit)
        if i % 2 == 0:
            tal_n = tal_n * 2
            LUHN = 9
            if tal_n > LUHN:
                tal_n = tal_n // 10 + tal_n % 10
        total = total + tal_n

    if total % 10 == 0:
        print("Valid Personnumer ✅")
    else:
        print("Not Valid Personnumer ❌")


def robber_language():
    word = input("Skriv ett ord: ")
    vowel = "AEIOUYÅÄÖ"
    resultat = ""
    for s in word:
        if s.lower() not in vowel and s.isalpha():
            resultat = resultat + s + "o" + s
        else:
            resultat = resultat + s
    print(f"{resultat}...")
