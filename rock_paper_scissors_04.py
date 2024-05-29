# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
comp = random.randint(0,2)
#print(comp)
player = int(input("choose 0=> rock, 1=> paper, 2=>scissors"))
#print(player)
if comp ==0 and player == 0 : 
    print("COMPUTER")
    print(rock)
    print("PLAYER")
    print(rock)
    print("*******************   TIE  ***********************")
if comp ==0 and player == 1 : 
    print("COMPUTER")
    print(rock)
    print("PLAYER")
    print(paper)
    print("************************WON****************************")
if comp ==0 and player == 2 : 
    print("COMPUTER")
    print(rock)
    print("PLAYER")
    print(scissors)
    print("************************LOST****************************")
if comp ==1 and player == 0 : 
    print("COMPUTER")
    print(paper)
    print("PLAYER")
    print(rock)
    print("************************LOST****************************")
if comp ==1 and player == 1 : 
    print("COMPUTER")
    print(paper)
    print("PLAYER")
    print(paper)
    print("************************TIE****************************")
if comp ==1 and player == 2 : 
    print("COMPUTER")
    print(paper)
    print("PLAYER")
    print(scissors)
    print("************************WON****************************")
if comp ==2 and player == 0 : 
    print("COMPUTER")
    print(scissors)
    print("PLAYER")
    print(rock)
    print("************************WON****************************")
if comp ==2 and player == 1 : 
    print("COMPUTER")
    print(scissors)
    print("PLAYER")
    print(paper)
    print("************************LOST****************************")
if comp ==2 and player == 2 : 
    print("COMPUTER")
    print(scissors)
    print("PLAYER")
    print(scissors)
    print("************************TIE****************************")



