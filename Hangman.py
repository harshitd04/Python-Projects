
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

import random
word_list = ["aardvark", "baboon", "camel"]
print("You Have 5 lives")
lives = 5
chosen_word = random.choice(word_list).lower()
original_word = chosen_word
blanks = ""
for i in range(len(chosen_word)):
    blanks += "_"
print(f"The word in blanks : {blanks}")
while lives > 0:
    check = input("Enter a letter to check: ").lower()
    if blanks == original_word:
        print("You Won!!!")
    elif check in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == check:
                blanks = blanks[:i] + check + blanks[i + 1:]  # Replace the specific index in blanks
                chosen_word = chosen_word[:i] + "_" + chosen_word[i + 1:]  # Replace the specific index in chosen_word

        print(f"Right choice!! \nYou have {lives} lives left.\nNow the word is : {blanks}\n\n")

    else:
        lives-=1
        print(f"Wrong Choice!! \nYou have {lives} lives left.\nThe word still is:  {blanks}\n\n")


if blanks != original_word:
    print(f"You Lost!!\nThe Word was {original_word}")




