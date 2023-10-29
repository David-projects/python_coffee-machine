def check_resources(drink, resources):
    """Checks the resources to see if there is the water, coffee, etc for the drink
    drink is the drink ordered
    resources are the current water, milk and coffee
    returns true if we have the resources and False if not"""
    
    if drink['ingredients']['water'] > resources['water']:
        print("Sorry there is not enough water.")
        return False
    elif drink['ingredients']['milk'] > resources['milk']:
        print("Sorry there is not enough milk.")
        return False
    elif drink['ingredients']['coffee'] > resources['coffee']:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


def value_of_coins(coins, value):
    """Works out the amount entered by times the numbers of coins with the value of the coins
    returns the value"""
    return round(coins * value, 2)


def take_money(cost):
    """Takes the money for the drink
    cost is the amount of the drink
    returns amount the mount taken or False if no money taken"""

    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = 0
    total += value_of_coins(quarters, 0.25)
    total += value_of_coins(dimes, 0.10)
    total += value_of_coins(nickles, 0.05)
    total += value_of_coins(pennies, 0.01)
    total = round(total, 2)

    print(f"You entered ${total}")
    
    if cost > total:
        print(f"You did not enter the right amount. You entered {total} the cost is {cost}. Money refunded")
        return False
    elif cost < total:
        change = round(total - cost, 2)
        print(f"Your change is {change}")
    
    return cost


def get_drink(meun):
    """Returns the drink the person wants"""
    drink = input("What would you like  (espresso/latte/cappuccino):").lower()

    if drink in meun:
        return drink

    print("You did not enter (espresso/latte/cappuccino) try again")
    get_drink(meun)

def get_report(resources, money):
    for key in resources:
        if key == 'water' or key == 'milk':
            print(f"{key}: {resources[key]} ml")
        else:
            print(f"{key}: {resources[key]} g")
    print(f"Money: ${money}")
