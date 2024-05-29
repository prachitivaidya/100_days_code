logo = """"""

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import  random

num = random.randint(0,100)
guess = 0

choice = input("Choose the level 'easy' or 'hard' : ")
if choice == "easy":
    guess = 10
else:
    guess = 5

while guess > 0 :
    print(f"Number of attempts left {guess}")
    gnum = int(input("Guess the number between 0-100 : "))

    if gnum == num:
        print("You win!!")
        break
        
    elif gnum > num:
        print("Too high guess lower!!")
        guess -=1
    else:
        print("Too low guess higher!!")
        guess -=1    

if guess ==0:
    print(f"You Loose the number was {num}")