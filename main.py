from collisionDetection import *
from displayScreen import *
from movement import move, movementKeyDetect
from os import system
from concurrent.futures import ThreadPoolExecutor # for detecting key presses asynchronously
from time import sleep


#refresh rate
refreshRate = 0.1
count = 0 # for the refresh rate so the screen doesnt look like its flashing

# space, in char, the snake can move in
height = 30
breadth = 50

# this dictionary will contain the coordinates of things to be drawn on the screen
# part:x,y
dictParts = {
        'O': [10,10], # head
        '@': [[9,10],[8,10]] # body
}

# data from movement
movementData = [0,1] # axis = (0 -> horizontal axis, 1 -> vertical axis), step = velocity of snake

# start detecting keys presses, exits when shift+s is pressed
keyDetect = ThreadPoolExecutor().submit(movementKeyDetect, movementData)

grid = createGrid(breadth, height)
createApple(breadth, height, dictParts)

run = startGameScreen()

while run:

    if count == 1:
        move(dictParts, movementData)
        count = 0

    if not (collision_with_wall(breadth, height, dictParts['O']) or collision_with_self(dictParts)):

        count += 1
        system('cls')
        #move(dictParts, movementData)
        printGrid(grid, dictParts, breadth, height)

        if collision_with_apple(dictParts['O'], dictParts['X']):
            del dictParts['X'] # removing old apple position
            createApple(breadth, height, dictParts) # creating a new position

        sleep(refreshRate)

    else:
        run = endGameScreen()
        if run:
            # reset variables
            dictParts = {
            'O': [10,10],
            '@': [[9,10],[8,10]]
            }
            movementData.clear()
            movementData.append(0)
            movementData.append(1)
            createApple(breadth, height, dictParts)
            count = 0


print("Type 'shift+s' to end the game")
