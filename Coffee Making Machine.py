MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

remaining_resources = resources
user_want = input("Enter what you want: ")
def ask_input():
    user_want = input("Enter what you want: ")
    return user_want

def print_remaining_resources(remaining_resources):
    for key in remaining_resources:
        print(f"{key} : {remaining_resources[key]}")

def take_money():
    quarters = int(input("Enter No. of quarters:"))
    dimes = int(input("Enter No. of dimes:"))
    nickles = int(input("Enter No. of nickles:"))
    pennies = int(input("Enter No. of pennies:"))
    total_money = (quarters * 0.25)+(dimes * 0.1)+(nickles * 0.05)+(pennies * 0.01)
    if total_money >= MENU[user_want]["cost"]:
        print(f"Money Refunded = {total_money - MENU[user_want]["cost"]}")
    else:
        print(f"Sorry that's not enough money. Payment Refunded = {total_money}")
        return False

def check_remaining_resources(remaining_resources):
    if user_want == "espresso":
        if remaining_resources["water"] < MENU[user_want]["ingredients"]["water"]  or remaining_resources["coffee"] < MENU[user_want]["ingredients"]["coffee"]:
            print("Not enough resources")
            return False
    elif remaining_resources["water"] < MENU[user_want]["ingredients"]["water"] or remaining_resources["milk"] < MENU[user_want]["ingredients"]["milk"] or remaining_resources["coffee"] < MENU[user_want]["ingredients"]["coffee"]:
        print("Not enough resources")
        return False
    else:
        return True

def deduct_remaining_resources(remaining_resources):
    if user_want == "espresso":
        remaining_resources["water"] -= MENU[user_want]["ingredients"]["water"]
        remaining_resources["coffee"] -= MENU[user_want]["ingredients"]["coffee"]
    else:
        remaining_resources["water"] -= MENU[user_want]["ingredients"]["water"]
        remaining_resources["coffee"] -= MENU[user_want]["ingredients"]["coffee"]
        remaining_resources["milk"] -= MENU[user_want]["ingredients"]["milk"]

def make_coffee():
    if take_money() == False or check_remaining_resources(remaining_resources)== False:
        return
    deduct_remaining_resources(remaining_resources)
    print(f"Here is your {user_want}")
    print(f"Remaining resources are: {remaining_resources}")

do_cont = False
while not do_cont:
    if user_want == "report":
        print_remaining_resources(remaining_resources)
        user_want = ask_input()

    elif user_want == "espresso" or user_want == "latte" or user_want == "cappuccino":
        make_coffee()
        user_want = ask_input()

    elif user_want == "end":
        print("Machine Closed.")
        do_cont = True

    else:
        print("Wrong Input")
        user_want = ask_input()








