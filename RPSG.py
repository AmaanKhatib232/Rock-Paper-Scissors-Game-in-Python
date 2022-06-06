'''
Hello Everyone!!!!
This is AMAAN KHATIB
from CSB - B3 - 55
VIT, Pune
'''

'''
The functions I have used are :
#gameStart()
#validGameStart()
#game(para1)
#gameWin(para1,para2)
#gameStats()
#validGameStats()
#gameEnjoy()
#validGameEnjoy()
#gameReplay()
#validGameReplay()
'''


import random
import time


########################################################################################################################
def game(gm):
    if gm == "yes":
        global playerwin, compwin, tied, numofsets, name
        playerwin = 0
        compwin = 0
        tied = 0

        name = str(input("\n    \t\t\t\tEnter your Name :\t"))
        numofsets = int(input("\n    \t\t\t\tHow many number of games do you want to play? :\t"))

        print("\n    \t\t\t\t##############################################################################\n")
        print("\n    \t\t\t\t--------------- GAME STARTED ---------------\t")

        for j in range(numofsets):
            print("\n\n    \t\t\t\tComp's turn: Rock(r), Paper(p), Scissors(s)?")
            user = input("\n    \t\t\t\tUser's turn: Rock(r), Paper(p), Scissors(s)?\t")
            user = user.lower()

            compChoice = random.randint(1, 3)

            if compChoice == 1:
                comp = 'r'
                c = 'Rock'
            elif compChoice == 2:
                comp = 'p'
                c = 'Paper'
            elif compChoice == 3:
                comp = 's'
                c = 'Scissor'

            if user == 'r':
                u = 'Rock'
            elif user == 'p':
                u = 'Paper'
            elif user == 's':
                u = 'Scissor'

            result = gameWin(comp, user)
            print("\n    \t\t\t\tComp choose --------", c)
            print("\n    \t\t\t\tUser choose --------", u)
            if result == None:
                print("\n    \t\t\t\tThe game is tied\n")
                tied = tied + 1
                print("    \t\t\t\t*****************************************\n")
            elif result == True:
                print("\n    \t\t\t\tYou win this game\n")
                playerwin = playerwin + 1
                print("    \t\t\t\t*****************************************\n")
            elif result == False:
                print("\n    \t\t\t\tYou lose this game\n")
                compwin = compwin + 1
                print("    \t\t\t\t*****************************************\n")

        # FUNCTION CALLING
        gameStats()


########################################################################################################################
def gameWin(comp, user):
    if user == comp:
        return None

    if comp == 'r':
        if user == 'p':
            return True
        elif user == 's':
            return False

    elif comp == 'p':
        if user == 'r':
            return False
        elif user == 's':
            return True

    elif comp == 's':
        if user == 'p':
            return False
        elif user == 'r':
            return True


########################################################################################################################
def validGameStats():
    print("\n    \t\t\t\tPlease enter valid input :)\t")
    print("\n    \t\t\t\t*************************************************************************\n")
    gameStats()


########################################################################################################################
def gameStats():
    print("\n    \t\t\t\t*************************************************************************\n")
    stats = str(input("\n    \t\t\t\tDo you want to see your statics(yes/no) : \t "))
    stats = stats.lower()

    if stats == "yes":
        print("    \t\t\t\t----------------------------------------")
        print(f"    \t\t\t\tThe game was played {numofsets} times")
        print("    \t\t\t\t----------------------------------------")
        print(f"    \t\t\t\t{name} won the game {playerwin} times")
        print("    \t\t\t\t----------------------------------------")
        print(f"    \t\t\t\t{name} lose the game {compwin} times")
        print("    \t\t\t\t----------------------------------------")
        print(f"    \t\t\t\tThe game tied {tied} times")
        print("    \t\t\t\t----------------------------------------\n")

        gameEnjoy()

    if stats == "no":
        gameEnjoy()

    else:
        validGameStats()


########################################################################################################################
def validGameEnjoy():
    print("\n    \t\t\t\tPlease enter valid input :)\t")
    print("\n    \t\t\t\t*************************************************************************\n")
    gameEnjoy()


########################################################################################################################
def gameEnjoy():
    print("\n    \t\t\t\t*************************************************************************\n")
    enjoy = input("\n    \t\t\t\tEnjoyed the Game (yes/no):) ? : \t\t\t")
    enjoy = enjoy.lower()
    if enjoy == "yes":
        gameReplay()
    if enjoy == "no":
        print("\n    \t\t\t\t\t\t\t*******************************\n     \t\t\t\t\t\t\t\t  THANK YOU\n    \t\t\t\t\t\t\t*******************************\n")
        time.sleep(3)
        quit()
    else:
        validGameEnjoy()


########################################################################################################################
def validGameReplay():
    print("\n    \t\t\t\tPlease enter valid input :)\t")
    print("\n    \t\t\t\t*************************************************************************\n")
    gameReplay()


########################################################################################################################
def gameReplay():
    print("\n    \t\t\t\t*************************************************************************\n")
    again = str(input("\n    \t\t\t\tDo you want to play again ? (yes/no) :\t"))
    again = again.lower()
    if again == "yes":
        print("\n    \t\t\t\t*************************************************************************\n")
        print("\n    \t\t\t\t---------- PLEASE FILL THE DETAILS :) ---------- \t\n")
        game(again)

    elif again == "no":
        print("\n    \t\t\t\t\t\t\t*******************************\n     \t\t\t\t\t\t\t\t  THANK YOU\n    \t\t\t\t\t\t\t*******************************\n")
        time.sleep(3)
        quit()
    else:
        validGameReplay()


########################################################################################################################
def validGameStart():
    print("\n    \t\t\t\tPlease enter valid input :)\t")
    print("\n    \t\t\t\t*************************************************************************\n")
    gameStart()


########################################################################################################################
def gameStart():
    gm = str(input("\n    \t\t\t\tAre you ready to play the game ? (yes/no) :\t"))
    gm = gm.lower()
    if gm == "yes":
        print("\n    \t\t\t\t*************************************************************************\n")
        print("\n    \t\t\t\t---------- PLEASE FILL THE DETAILS :) ---------- \t\n")
        game(gm)

    elif gm == "no":
        print("\n    \t\t\t\t\t\t\t*******************************\n     \t\t\t\t\t\t\t\t  THANK YOU\n    \t\t\t\t\t\t\t*******************************\n")
        time.sleep(3)
        quit()
    else:
        validGameStart()


########################################################################################################################
########################################################################################################################
########################################################################################################################


# THE GAME WILL START FROM HERE #

print("\n    \t\t\t\t\t\t\t:::::::::::::::::::::::::::::::::::::::::::\n    \t\t\t\t\t\t\t\t!!HELLO EVERYONE!!")
print("\n    \t\t\t\t\t\t\tI am AMAAN KHATIB - Developer of this game\n    \t\t\t\t\t\t\t:::::::::::::::::::::::::::::::::::::::::::\n")
print("\n    \t\t\t\t\t\t\t::::::::::::::::::::::::::::::::::\n    \t\t\t\t\t\t\t\tWELCOME TO THE GAME\n    \t\t\t\t\t\t\t::::::::::::::::::::::::::::::::::\n")
print('    \t\t\t <<<<<<<<< \n    \t\t\t\tRULES    \n\t\t\t\t >>>>>>>>>')
print('\n   \t\t\t\t You Have Three Choices :\n    \t\t\t\t Rock Paper Scissor.\n    \t\t\t\t You Have To Enter r / p / s for Rock Paper Scissor Respectively.'
    '\n\n    \t\t\t\t<<<< Gamewinning>>>>:\n\n   \t\t\t\t\t'
    '1. If User Choose Rock And The Computer Choose Scissor Then User Will Win.\n    \t\t\t\t'
    '2. If User Choose Paper And The Computer Choose Rock Then Also User Will Win\n    \t\t\t\t'
    '3. If User Choose Scissor And The Computer Choose Paper Then User Will Win\n    \t\t\t\t'
    '4. If User Choose Paper And The Computer Choose Scissor Then User Will Lose\n    \t\t\t\t'
    '5. If User Choose Rock And The Computer Choose Paper Then User Will Lose\n    \t\t\t\t'
    '6. If User Choose Scissor And The Computer Choose Rock Then User Will Lose \n\n   \t\t\t\t '
    '* If The Choices Of Both User and Computer Will Be Same Then The Game Will Be Tied.\n\n ')

gameStart()