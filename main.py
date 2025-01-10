from data import resources, MENU

def print_resources():
    """Prints all the actual resources in coffee machine"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${float(profit)}")

def is_resources_sufficient(drink_resources, machine_resources):
    """Returns True if machine has enough resources, otherwise False"""
    for resource in drink_resources:
        if drink_resources[resource] > machine_resources[resource]:
            print(f"Sorry, there is not enough {resource}.")
            return False
    return True

def process_coins(drink_cost):
    """Returns True if the user inserted enough money, otherwise False"""
    total = int(input("How many quarters do you want to insert?: ")) * 0.25
    total += int(input("How many dimes do you want to insert?: ")) * 0.1
    total += int(input("How many nickles do you want to insert?: ")) * 0.05
    total += int(input("How many pennies do you want to insert?: ")) * 0.01

    if total >= drink_cost:
        global profit
        profit += drink_cost
        change = round(total - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(guest_choice, drink_resources, machine_resources):
    """Deduct all the ingredients for the drink in coffee machine"""
    for ingredient in machine_resources:
        if ingredient in drink_resources:
            machine_resources[ingredient] -= drink_resources[ingredient]
    print(f"Here is your {guest_choice} ☕️. Enjoy!")

profit = 0
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print_resources()
    elif choice in MENU:
        drink = MENU[choice]
        if is_resources_sufficient(drink['ingredients'], resources):
            if process_coins(drink['cost']):
                make_coffee(choice, drink['ingredients'], resources)
    else:
        print("Invalid choice. Please select a valid option.")