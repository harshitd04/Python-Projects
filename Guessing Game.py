import random
num = random.randint(1,100)

difficulty = input("Choose your difficulty \"h\" for hard and \"e\" for easy\nEnter your difficulty : ")
if difficulty == "h":
    lives = 5
elif difficulty == "e":
    lives = 10
else:
    print("Wrong Input. ")

def guess_game(lives, num):
    while lives > 0:
        guess = int(input("Enter your guess: "))
        if guess == num:
            print("You win. Right Choice.")
            return
        elif guess > num:
            print("Go lower")
            lives -= 1
            print(f"Remaining lives = {lives}\n-----------------------")
        elif guess < num:
            print("Go higher")
            lives -= 1
            print(f"Remaining lives = {lives}\n-----------------------")
        else:
            print(f"You lost. The number was {num}")
guess_game(lives, num)