def print_stock():
    """Prints the stock of the coffee machine"""

    global water_stock
    global milk_stock
    global beans_stock
    global cups_stock
    global money_stock

    print("""The coffee machine has:
    {} of water
    {} of milk
    {} of coffee beans
    {} of disposable cups
    {} of money""".format(water_stock, milk_stock, beans_stock, cups_stock, money_stock))


def buy_action():
    """Buy feature of the coffee machine"""

    global water_stock
    global milk_stock
    global beans_stock
    global cups_stock
    global money_stock

    drinks = {1: {"name": "espresso", "water": 250, "milk": 0, "beans": 16, "price": 4},
              2: {"name": "latte", "water": 350, "milk": 75, "beans": 20, "price": 7},
              3: {"name": "cappuccino", "water": 200, "milk": 100, "beans": 12, "price": 6}}

    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    choice = int(input())

    water_stock -= drinks[choice]["water"]
    milk_stock -= drinks[choice]["milk"]
    beans_stock -= drinks[choice]["beans"]
    cups_stock -= 1
    money_stock += drinks[choice]["price"]


def fill_action():
    """Buy feature of the coffee machine"""

    global water_stock
    global milk_stock
    global beans_stock
    global cups_stock
    global money_stock

    print("Write how many ml of water do you want to add:")
    water_add = int(input())
    print("Write how many ml of milk do you want to add:")
    milk_add = int(input())
    print("Write how many grams of coffee beans do you want to add:")
    beans_add = int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    cups_add = int(input())

    water_stock += water_add
    milk_stock += milk_add
    beans_stock += beans_add
    cups_stock += cups_add


def take_action():
    """Take feature of the coffee machine"""

    global money_stock

    print("I gave you ${}".format(money_stock))

    money_stock = 0


def action_taker():
    """Executes a feature based on an input"""

    print("Write action(buy, fill, take):")
    action = input()

    if action == 'buy':
        buy_action()
    elif action == 'fill':
        fill_action()
    elif action == 'take':
        take_action()


water_stock = 400
milk_stock = 540
beans_stock = 120
cups_stock = 9
money_stock = 550

print_stock()
print("")
action_taker()
print("")
print_stock()
