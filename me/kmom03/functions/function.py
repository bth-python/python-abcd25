# functions Övningar
def hello():  # en funktion som skriver ut ett meddelande
    print("Hellå där och välkommen")


print("Startar programmet")
hello()


def hello_person(name):  # funktion som hälar person
    print(f"Hello {name} , kul å ser dig")


hello_person("Hussain")
hello_person("Karimi")


def hello_language(name, language="sv"):
    if language == "sv":
        print(f"Hej {name}")
    elif language == "en":
        print(f"Hello {name}")
    else:
        print(f"Unknown language, hej {name} !")


hello_language("Ali")
hello_language("Sara", "en")


def circle_area(radie):
    area = 3.14 * radie**2
    return area


rad = 12
result = circle_area(rad)
print(f"Circle med radie {rad}, har arean {result}")


# 2 funktioner en beräkna area andra skriva ut den
def c_area(radius):
    return 3.14 * radius**2


def print_area(radius):
    area = c_area(radius)
    print(f"En cirkel med radie {radius} har en area på {area: 2} kvadradmeter")


print_area(3)
print_area(12)


# beräknar buss biljetter
def ticket_price(age, distance, base_price):
    price = base_price * distance

    if age < 18:
        price = price * 0.5
    elif age > 65:
        price = price * 0.7
    return price


print(f"Ung betalar: {ticket_price(15, 10, 2)} kr")
print(f"Vuxen betalar: {ticket_price(30, 10, 2)} kr")
print(f"Pensioner betalar: {ticket_price(70, 10, 2)} kr")


# LEGB regeln och scopes i Python


def fun():
    x = "lokal"
    print(x)


fun()

x = "global"


def fun():
    x = "lokal"
    print("funktionen gäller ", x)


fun()
print("funktionen gäller ", x)


x = "global"


def fun():
    global x
    x = "ändrad global"
    print("funktionen är ", x)


fun()
print("funktionen är ", x)

x = 12


def fun():
    global x
    x = 18
    print(x)


fun()
print(x)

x = 100


def fun():
    x = 50
    print(x)


fun()
print(x)

x = 10


def add_one():
    global x
    x = x + 1


def add_two():
    global x
    x = x + 2


add_one()
print("första add blir då: ", x)

add_two()
print("andra add blir då: ", x)


x = 0


def add_1():
    global x
    x = x + 1
    print("efter add 1: ", x)


def add_2():
    global x
    x = x + 12
    print("efter add 2: ", x)


def multi():
    global x
    x = x * 3
    print("efter multi: ", x)


add_1()
add_2()
multi()
add_2()


x = 1
y = 2


def fun():
    global x, y
    x = x + y
    y = y * 2

    print(f"x = {x}, y = {y}")


fun()  # x = 3, y = 4
fun()  # x = 7, y = 8
fun()  # x 15, y = 16

x = 5  # global


def outer():
    x = 10

    def inner():
        global x
        x = x + 1
        print("I inner (global x):", x)

    inner()
    print("I outer (enclosing x):", x)


outer()
print("I global:", x)


counter = 0


def rekursiv_add(n):
    global counter
    if n > 0:
        counter = counter + n
        rekursiv_add(n - 1)


rekursiv_add(10)
print("summan är: ", counter)

x = 0


def adding(n):
    global x
    x = x + n
    print("x = ", x)


while True:
    val = input("skriv ett tal eller Enter q för att avsluta: ")
    if val == "q":
        break

    try:
        nummer = int(val)
        adding(nummer)

    except ValueError:
        print("Not a valid choice!")
print("Ha det så bra lyckades")
