# Kmom01 Uppgift 1.......................
print("Hello & Welcome to the unit converter")
value = input("Enter a value to convert: ")  # ber användaren skriva ett tal
if not value.isdigit():  # om skrivningen inte va ett tal, kasta ut detta meddelande
    print("Invalid value, Enter a number: ")
    exit()

value = int(value)  # bytar till int data typen

converter = input(  # ber user att välja sitt val
    "Choose what u want to convert:\n"
    "P: Price, before --> after discount and tax\n"
    "S: Speed, km/h --> mph\n"
)
converter = converter.upper()  # kontrollerar bokstäver
if converter == "P":
    price = (value - 10) * 1.2  # user's inmatning med 10% rabat + 20% tax
    print(
        f"The final price of {float(value): .2f} after 10 kr discount "
        f"and 20% tax is: {price:.2f} kr"
    )
elif converter == "S":
    mph = value * 0.62137  # km/h byts till mph
    print(f"{float(value): .1f} km/h is equivalent to {mph: .2f} mph")
else:
    print("Invalid converter, please enter P or S.")
    exit()  # avsluta
