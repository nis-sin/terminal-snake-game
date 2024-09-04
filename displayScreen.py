# this file is for displaying things on screen
'''
NOTE:

f-strings padding;
x = "test"
f'{x:>10}' -> '   test'
f'{x:*<8}' -> 'test****'
f'{x:=^8}' -> '==test=='
x, n = 'test',10
f'{x:~^{n}}' -> '~~~test~~~'
n = length of string, len(string) can never > n
'''

import sys
from os import system
from random import randint
from keyboard import read_key
from time import sleep


def createGrid(breadth, height):

    # creating the grid

    dashedLine = '-'*(breadth+2) # for the top and bottom border of the grid
    grid       = dashedLine + '\n'

    for _ in range(1,height+1):
        grid = grid + f"|{'':>{breadth}}" + "|\n"

    grid = grid + dashedLine

    return grid


def createApple(breadth, height, dictParts):
    appleCoordinates = [randint(2,breadth),randint(2,height)]
    while appleCoordinates == dictParts['O'] or appleCoordinates in dictParts['@']: # checking if apple coord == coords of '@' or 'O'
        appleCoordinates = [randint(2,98),randint(2,height)]
    dictParts['X'] = appleCoordinates


def printGrid(grid, dictParts, breadth, height):

    for part, coord in dictParts.items():

        if part != '@':

            tempGrid = grid[:(breadth+2)+(coord[1]-1)*(breadth+3)+(coord[0]+1):]
            # format: len(line 1) (== breadth+2) + no. of rows to move according to the y value + x coord of the part + 1 (because each line contain a '|' at the beginning of the line)
            # (int(coord[1])-1) because 1 <= y coordinate <= height, so need to - 1
            # (breadth+3) because from line 1-height there are '|' at the beginning and end, and a '\n' which counts a 1 char

            tempGrid = tempGrid + part # adding 'part' to grid

            grid = grid[(breadth+2)+(coord[1]-1)*(breadth+3)+(coord[0]+1)+1::]
            # format: len(line 1) (== breadth+2) + no. of rows to move according to the y value + x coord of the part + 1 (because each line contain a '|' at the beginning of the line) + len(part) (== 1)

            grid = tempGrid + grid # after adding 'part'

        else:

            for point in coord: # value of '@' is a 2d list
                tempGrid = grid[:(breadth+2)+(point[1]-1)*(breadth+3)+(point[0]+1):]
                tempGrid = tempGrid + '@'
                grid     = grid[(breadth+2)+(point[1]-1)*(breadth+3)+(point[0]+1)+1::]
                grid     = tempGrid + grid

    print(grid)


def startGameScreen():
    response = ''
    while response not in ('y','n'):
        print("""\n\n\n
        Put your terminal on FULL SCREEN.

        HOW TO PLAY:

        - 'a' and 'd' are the movement keys.
        - 'O' is the head of the snake, '@' is the body of the snake, 'X' is the food to grow the snake by 1 '@'
        - Don't collide with the walls and yourself.

        OBJECTIVE:

        - Go from short boy to long man.

        NOTE:

        - When trying to navigate, put yourself in the shoes of the snake...... or scales of the snake.
          Eg: when the snake is moving rightwards, pressing 'a' will cause the snake to move up, pressing 'd' will cause it to move down.

        - IMPORTANT: DON'T press 'shift+s' while you are playing, or else you will not be able to move the snake! (it's not a bug, it's a feature :D ).
          However, after you have played the game, you will asked to press 'shift+s', in this case, do follow the instructions.
        
        - After you have played, your terminal prompt may have a random strings of 'a's and 'd's, no worries, you can simply delete them
          (Yes, this is a feature too :D).

        Ready? Y/N
        \n\n\n""")
        response = read_key().lower()
        sys.stdout.write(u"\u001b[2J") # clear screen
        sys.stdout.write(u"\u001b[H")  # Cursor up one line

    if response == 'y':
        for i in range(3,0,-1):
            print(f"{i}...")
            sleep(1)
        return True
    else:
        print(":(")
        return False


def endGameScreen():
    response = ''
    while response not in ("y","n"):
        print("""\n\n\n
        \t\t\tRestart game? Y/N
        \n\n\n""")
        response = read_key().lower()
        sys.stdout.write(u"\u001b[2J") # clear screen
        sys.stdout.write(u"\u001b[H")  # Cursor up one line

    return response == 'y'
