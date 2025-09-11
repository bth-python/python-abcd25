# Kmom01 Uppgift 1.......................
print("Hello & Welcome to the unit converter")
value = input("Enter a value to convert: ")
if not value.isdigit():
    print("Invalid vakue, Enter a number: ")
    exit()

value = int(value)

converter = input(
    "Choose what u want to convert:\n "
    "P: Price, before --> after discount and tax\n"
    "S: Speed, km/h --> mph\n"
)
converter = converter.upper()
if converter == "P":
    price = (value - 10) * 1.2
    print(
        f"The final price of {float(value): .2f} after 10 kr discount and 20% tax is: {price: .2f} kr"
    )
elif converter == "S":
    mph = value * 0.62137
    print(f"{float(value): .2f} km/h is equivalent to {mph: .2f} mph")
else:
    print("Invalid converter, please enter P or S.")
    exit()
