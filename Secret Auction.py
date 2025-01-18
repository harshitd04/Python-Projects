import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

bid_dic = {}
cont = False
while not cont:
    name = input("Enter your name: \n")
    amount = int(input("Enter your bid: \n"))
    bid_dic[name] = amount

    check = input(f"Do you want to continue adding more people? \"yes\" to continue, \"no\" to stop: \n")
    if check == "no":
        cont = True
    clear_screen()

max_amount = 0
max_name = ["max_name"]
for key in bid_dic:
    if bid_dic[key] > max_amount:
        max_amount = bid_dic[key]
        max_name[0] = key
winner_name = max_name[0]
print(f"The winner is {winner_name} who has bidded at {max_amount}!!!")