from collections import Counter

"""
Marvin, vännen i terminal
"""

print(r"""
        ^
       /^\
      /___\
     |=   =|
     |     |
     |     |
     |     |
     |     |
     |     |
    /|##!##|\
   / |##!##| \
  /  |##!##|  \
 |  / ^ | ^ \  |
 | /  ( | )  \ |
 |/   ( | )   \|
     ((   ))
    ((  :  ))
    ((  :  ))
     ((   ))
      (( ))
       ( )
        .
        .
        .
""")
print("Hej, Här har du Marvin, hjälpsamma robot som hjälper dig 🦾")

while True:  # main loop som visar upp menyn å kontrollerar user's val
    print("\nMeny")
    print("1. Skriv ditt namn")
    print("2. Change Temperature Celsius → Fahrenheit")
    print("3. Poäng till betyg")
    print("4. Jämför tal: ")
    print("5. Skriv in personnummer")
    print("6. Rovarspråket")
    print("q. Avsluta")

    # låt användaren göra sitt val
    val = input("Välja ett alternativ: ")
    if val == "q":  # om inmatningen gäller inte "q", ta else meddelandet
        GREEN = "\033[32m"
        RESET = "\033[0m"
        print(f"{GREEN}Hejdå från roboten 👋{RESET}")
        break  # avslutar programmet

    elif val == "1":
        GREEN = "\033[32m"
        RESET = "\033[0m"
        print(f"{GREEN}Hej Ali heter jag, å Robot hälsar dig tillbaka 🤚{RESET}")

    elif val == "2":
        GREEN = "\033[32m"
        RESET = "\033[0m"
        # ta inmatningen, omvandla den till decimal float
        celcius = float(input(f"{GREEN}Skriv temperaturen i Celcius: {RESET}"))
        fahrenheit = round((celcius * 9 / 5) + 32, 2)  # runda decimalen till 2
        print(f"{celcius} °C Celcius motsvarar {fahrenheit: 2} °F Fahrenheit")

    elif val == "3":
        max_poang = float(input("Ange Max poang: "))  # example 169
        din_poang = float(input("Ange dina poang: "))  # example 59
        procent = (din_poang / max_poang) * 100  # 59/169 = 0.349 * 100 = 34.9

        GRADE_A = 90
        GRADE_B = 80
        GRADE_C = 70
        GRADE_D = 60
        GRADE_E = 50

        # if procent >= 90: ERROR, Ruff tycker globala konstanter måste va med UPPER CASE,
        # alltså upper snake case som ska användas i mitt fall
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
        GREEN = "\033[32m"
        RESET = "\033[0m"
        print(f"{GREEN}Betyg: {betyg}{RESET}")

    elif val == "4":
        # föregående variabel som sparar tal för jämföelse,
        # börjar som none/inget för att inget tal matats än.
        old_value = None

        while True:
            GREEN = "\033[32m"
            RESET = "\033[0m"
            # tar en input från användaren
            value = input(f"{GREEN}skriv ett tal eller (skriv done för att avsluta): {RESET}")
            if value == "done":
                break  # loopen stoppas medan inmatningen skrivs klar
            try:
                # omvandla input till float, annars hoppa över except meddelande
                tal = float(value)
                if old_value is None:
                    old_value = tal
                    continue  # försätt
                if tal > old_value:
                    print(f"{tal} is larger than {old_value}")
                elif tal < old_value:
                    print(f"{tal} is smaller than {old_value}")
                else:
                    print("same")
                old_value = tal

            except ValueError:  # s124❌ dfhdf❌ 4124✅
                print("Not a number")

    elif val == "5":
        GREEN = "\033[32m"
        RESET = "\033[0m"
        personnummer = input(f"{GREEN}Skriv in personnummer: {RESET}").replace("-", "")
        LENGHT_PERSONNUMMER = 10
        # om personnummer inte en siffra FEL
        if not personnummer.isdigit() or len(personnummer) != LENGHT_PERSONNUMMER:
            RED = "\033[31m"
            RESET = "\033[0m"
            print(f"{RED}Not a valid personnummer{RESET}")
            continue  # försätt till nästa iteration
        total = 0  # summering variabel enligt Luhn algorithm
        # gå genom varje siffra i personnummer i å värdet är digit
        for i, digit in enumerate(personnummer):
            tal_n = int(digit)  # omvandla siffran från sträng till heltal
            if i % 2 == 0:  # varje siffra som är jämna index bearbetas
                tal_n = tal_n * 2  # multipliceras siffran med 2
                LUHN = 9  # if result greater than 9, addera ihop siffror
                if tal_n > LUHN:
                    tal_n = tal_n // 10 + tal_n % 10
            total = total + tal_n  # lägger siffran till den totala summan

        if total % 10 == 0:  # kontroll om siffran är modulus 10
            GREEN = "\033[32m"
            RESET = "\033[0m"
            print(f"{GREEN}Valid Personnumer ✅{RESET}")
        else:
            RED = "\033[31m"
            RESET = "\033[0m"
            print(f"{RED}Not Valid Personnumer{RESET}")
    elif val == "6":
        word = input("Skriv ett ord: ")  # ber skriva skrva nåt
        vowel = "AEIOUYÅÄÖ"
        resultat = ""  # result string
        for s in word:  # gå in i varje bokstav i ordet
            if s.lower() not in vowel and s.isalpha():  # omd det är inte en vowel å är en bokstav
                resultat = resultat + s + "o" + s  # lägger in ö bokstav igen
            else:
                resultat = resultat + s
        GREEN = "\033[32m"
        RESET = "\033[0m"
        print(f"{GREEN}{resultat}{RESET}")

    else:
        RED = "\033[31m"
        RESET = "\033[0m"
        print(f"{RED}Alternativet {val} finns ej med i listen..!{RESET}")

# EXTRA UPPGIFT, tar in 2 stränger, gör om t små bokstäver
string_one = input("Skriv din första strängen: ").lower()
string_two = input("Skriv din andra strängen: ").lower()

# beräknar hur många gånger varje str finns i båda stränger
count_str_one = Counter(string_one)
count_str_two = Counter(string_two)

match = True  # anta att vi först matchar
# kontrollerar varje bokstav i den andra strängen
for letter, antal in count_str_two.items():
    if count_str_one[letter] < antal:  # om det finns tillräcklig gånger NO MATCH
        match = False
        break  # avbryt
if match:  # om det stämmer skriv ut match annars no match
    GREEN = "\033[32m"
    RESET = "\033[0m"
    print(f"{GREEN}Matching ...{letter} finns med i första strängen {RESET}")
else:
    RED = "\033[31m"
    RESET = "\033[0m"
    print(f"{RED}Not Matching.{RESET}")
