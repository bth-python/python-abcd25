import sys

summan = int(input("Vad är summan: "))
personer = int(input("Hur många personer som ska dela på: "))

if personer <= 0:  # kontrollllllllllll
    print("Warning! antal personer måste va minst 1")
    sys.exit(1)

per_pers = summan / personer
print(f"Varje person ska betala {per_pers: .2f} kr ")
