MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

resources_to_check = ["water", "milk", "coffee"]


def check_levels(resource_to_check):
    for i in resources_to_check:
        if MENU[selection]["ingredients"][i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


def process_money(selection):
    print(f'The cost of {selection} is £{MENU[selection]["cost"]}')
    print('Please insert coins:')
    total_coins = float(input("How many £1 coins?\n"))
    total_coins += float(input("How many 50p pieces?\n")) * 0.5
    total_coins += float(input("How many 20p pieces?\n")) * 0.2
    total_coins += float(input("How many 10p pieces?\n")) * 0.1
    return total_coins

money = 0.0
machine = True
while machine:
    selection = input("What would you like? (espresso/latte/cappuccino)\n").lower()
    if selection == 'report':
        print(f'''
Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: ${money}
''')
    elif selection == 'off':
        machine = False
    elif selection == 'espresso' or selection == 'latte' or selection == 'cappuccino':
        if check_levels(MENU[selection]["ingredients"]):
            customer_money = process_money(selection)
            if customer_money >= MENU[selection]["cost"]:
                money += MENU[selection]["cost"]
                change = round((customer_money - MENU[selection]["cost"]), 2)
                print(f'Enjoy your {selection}, your change is £{change}')
                for n in resources_to_check:
                    resources[n] = resources[n] - MENU[selection]["ingredients"][n]
            elif customer_money < MENU[selection]["cost"]:
                print(
                    f'You have not added enough money. You inserted £{customer_money}, the cost of {selection} is £{MENU[selection]["cost"]}')

    else:
        print("Incorrect selection. Please remake selection")
