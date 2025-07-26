#!/usr/bin/evn python3

"""
Program som tar emot ett numeriskt värde och omvandlar det enligt användarens val:
- Pris (före → efter rabatt och moms)
- Hastighet (km/h → mph)
"""

print("Hello and welcome to the unit converter!")

"""
Extra:
 - små boktäver i input
 - try except för att fånga felaktiga inmatningar
"""
# Försök läsa in ett tal från användaren
try:
    inp_to_convert = input("Enter value to convert: ")
    value_to_convert = float(inp_to_convert)

except ValueError:
    print("Invalid value, please enter a number.")
    exit()

# Fråga vad som ska konverteras
msg = (
    "Choose what to convert:\nP: Price, before --> after discount and tax\nS: Speed, km/h --> mph\n"
)
convert_type = input(msg)
convert_type = convert_type.lower()  # Gör valet skiftlägesokänsligt

# Prisomvandling
if convert_type == "p":
    discount = 10
    taxrate = 0.2
    final_price = round((value_to_convert - discount) * (1 + taxrate), 2)
    print_str = (
        f"The final price of {value_to_convert} after 10kr discount"
        f" and 20% tax is: {final_price} kr"
    )

# Hastighetsomvandling
elif convert_type == "s":
    mph = round(value_to_convert * 0.62137, 2)
    print_str = f"{value_to_convert} km/h is equivalent to {mph} mph"

# Ogiltigt val
else:
    print(convert_type + "Invalid converter, please enter P or S." + inp_to_convert)
    exit()

# Skriv ut resultat
print(print_str)
