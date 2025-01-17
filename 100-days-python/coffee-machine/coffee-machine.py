MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
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

powered_on = True

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0.0

def choose_brew():
    """
    Asks the customer to choose what kind of drink they would like
    If they make a typo, it asks again.
    """
    choice = input("What would you like? (espresso ($1.50)/latte ($2.00)/cappuccino ($3.00)): ").lower()
    if choice == "espresso" or choice == "latte" or choice == "cappuccino" or choice == "off" or choice == "report":
        return choice
    else:
        print("Invalid input. Check spelling.")
        return choose_brew()

def check_resources(drink, inv_water, inv_milk, inv_coffee):
    """
    When the user choose a drink, check if there are enough resources for water, milk, and coffee
    I decided to use a nested array to avoid including an additional loop
    """
    order_ingredients = [
        ["milk"  , inv_milk  , drink["ingredients"]["milk"]  ],
        ["water" , inv_water , drink["ingredients"]["water"] ],
        ["coffee", inv_coffee, drink["ingredients"]["coffee"]]]
    ingredient_check = []

    for ingredient in order_ingredients:
        if ingredient[1] - ingredient[2] >= 0:
            ingredient_check.append(True)
        else:
            print(f"There is not enough {ingredient[0]}.  Please select a different drink.")
            ingredient_check.append(False)

    return ingredient_check

def coin_insert():
    """
    If there are sufficient resources to make the drink selected, the user is prompted to insert their coins.
    Calculates the monetary value of the coins and returns it.
    """
    payment = 0
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * .25
    dimes = int(input("How many dimes? ")) * .1
    nickels = int(input("How many nickels? ")) * .05
    pennies = int(input("How many pennies? ")) * .01
    payment += quarters + dimes + nickels + pennies
    return payment

def refund_excess(customer_payment, cost):
    """
    Calculates the amount to be refunded to the customer
    If the refund is negative, there is not enough money and it returns their coins.
    If the refund is positive or 0, it will add the money to the global variable
    """
    global money
    refund = customer_payment - cost

    if refund < 0:
        print("Insufficient coins, refunding full amount.")
    else:
        print(f"Here is your ${round(refund, 2)} in change.")
        money += cost
        print("Here is your espresso ☕️. Enjoy!")
        return True

def remove_materials(drink):
    global water, milk, coffee
    print(drink)
    water -= drink["water"]
    milk -= drink["milk"]
    coffee -= drink["coffee"]

while powered_on:
    choice = choose_brew()
    if choice == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money ${money}")
    elif choice == "off":
        powered_on = False
    else:
        available_ingredients = check_resources(MENU[choice], water, milk, coffee)
        if all(available_ingredients):
            payment = coin_insert()
            successful = refund_excess(payment, MENU[choice]["cost"])
            if successful:
                remove_materials(MENU[choice]["ingredients"])
        else:
            choose_brew()
