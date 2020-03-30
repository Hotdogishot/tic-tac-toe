#Coded by Amessuo
#https://github.com/Hotdogishot
#IG: Oussema_wama

#IMPORTS
import os
from colorama import init 
from termcolor import colored
#Global variable
clear = lambda: os.system('cls')
spot = ['1','2','3','4','5','6','7','8','9']
used = []
current_player = ''
#Print Tic tac toe table
def table():
    print('+---+---+---+')
    print('| ' + spot[0] + ' | ' + spot[1] + ' | ' + spot[2] + ' |')
    print('+---+---+---+')
    print('| ' + spot[3] + ' | ' + spot[4] + ' | ' + spot[5] + ' |')
    print('+---+---+---+')
    print('| ' + spot[6] + ' | ' + spot[7] + ' | ' + spot[8] + ' |')
    print('+---+---+---+')
#Pick the spot
def pick(player):
    CMD = 0
    if (player == 'X'):
        color = 'green'
    else:
        color = 'red'
    table()
    while(True):
        CMD = int(input(player + ' player choose spot: '))
        if (CMD not in used) and (CMD in range(1,10)):
            break
    spot[CMD-1] = colored(player,color)        
    clear()
    return used.append(CMD)
#Check if there is a winner and return it
def winner():
    argument = True
    switcher = {
        spot[0] == spot[3] == spot[6] : spot[0],
        spot[1] == spot[4] == spot[7] : spot[1],
        spot[2] == spot[5] == spot[8] : spot[2],
        spot[0] == spot[1] == spot[2] : spot[0],
        spot[3] == spot[4] == spot[5] : spot[3],
        spot[6] == spot[7] == spot[8] : spot[6],
        spot[0] == spot[4] == spot[8] : spot[0],
        spot[6] == spot[4] == spot[2] : spot[6],
    }
    return switcher.get(argument, False)
def main():
    #Choose X|O
    while(True):
     CMD = str(input('Player 1 Choose X/O: ')).upper()
     if (CMD == 'X') or (CMD == 'O'):
         break
    if (CMD == 'X'):
     current_player = 'X'
    else:
     current_player = 'O'
    #Start playing
    for i in range(0,len(spot)):
        if (current_player == 'X'):
         pick('X')
         current_player = 'O'
        else:
         pick('O')
         current_player = 'X'
        if (winner() != False):
            print(winner() + ' Player is the winner!')
            break
        if (i == len(spot)-1):
            table()
            print('Game Over!')
    stay = input('Press any key to continue . . .')    
if __name__ == "__main__":
    #Print Ascii Logo
    print('+-------------+')
    print('| Tic tac toe |')
    print('+-------------+')
    #Start the game
    main()