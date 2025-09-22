import marvin1

def main():
    print(r"""
        .===========.
    |   |       |
    |  /|\      |
    | /a|d\     |
    |___________|
    |_________-_|_,-.
    [_____________]   )
    .,,,,,,,,,, ,,.  (_
    /,,,,,,,,,,, ,,,\ (>`\
    (______.-``-._____) \__)
    """)
    print("Hej, Här har du Marvin, hjälpsamma robot som hjälper dig 🦾")

    while True:
        print("\nMeny")
        print("1. Skriv ditt namn")
        print("2. Change Temperature Celsius → Fahrenheit")
        print("3. Poäng till betyg")
        print("4. Jämför tal: ")
        print("5. Skriv in personnummer")
        print("6. Rovarspråket")
        print("q. Avsluta")

        val = input("Välja ett alternativ: ")

        if val == "q":
            GREEN = "\033[32m"
            RESET = "\033[0m"
            print(f"{GREEN}Hejdå från roboten 👋{RESET}")
            break
        if val == "1":
            marvin1.greet()
        elif val == "2":
            marvin1.celsius_to_fahrenheit()
        elif val == "3":
            marvin1.points_to_grade()
        elif val == "4":
            marvin1.compare_number()
        elif val == "5":
            marvin1.validate_ssn()
        elif val == "6":
            marvin1.robber_language()
        else:
            RED = "\033[31m"
            RESET = "\033[0m"
            print(f"{RED}Alternativet {val} finns ej med i listen..!{RESET}")

if __name__ == "__main__":
    main()
