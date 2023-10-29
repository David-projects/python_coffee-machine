from drinks import MENU #import the drinks menu
from resources import resources
import coffee_functions


print("Welcome to the coffee machine")

want_drink = 'y'
money_total = 0


while want_drink == 'y':
    drink = coffee_functions.get_drink(MENU)
    print(drink)
    if coffee_functions.check_resources(MENU[drink], resources):
        money_taken = coffee_functions.take_money(MENU[drink]['cost'])
        print(f"money returned {money_taken}")
        if money_taken:
            money_total += money_taken
            print(f"Here is your {drink}")
            resources['coffee'] -= MENU[drink]['ingredients']['coffee']
            resources['water'] -= MENU[drink]['ingredients']['water']
            if not drink == 'espresso':
                resources['milk'] -= MENU[drink]['ingredients']['milk']

    want_drink = input("Would you like a other drink n/y").lower()
    if want_drink == 'n':
        coffee_functions.get_report(resources, money_total)


        


    


        