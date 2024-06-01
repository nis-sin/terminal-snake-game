# this file is for movement of the snake

from keyboard import wait, add_hotkey # key presses are detected immediately without having to press enter
from collisionDetection import collision_with_apple


def move(dictParts, movementData):

    tempCoord = dictParts['O'].copy()

    dictParts['O'][movementData[0]] += movementData[1] # moving the snake

    if dictParts.get("@", 0):
        for i in range(len(dictParts['@'])):
            dictParts['@'][i], tempCoord = tempCoord.copy(), dictParts['@'][i].copy()

    if collision_with_apple(dictParts['O'], dictParts['X']):
        dictParts['@'].append(tempCoord)


def movementKeyDetect(movementData):
    add_hotkey('a', lambda: turning('a', movementData))
    add_hotkey('d', lambda: turning('d', movementData))
    wait('shift+s') # function exits when shift+s is pressed


def turning(key, movementData):
    if movementData[0]: # checking if snake on y-axis
        if key == 'd':
            movementData[1] = movementData[1]*(-1) # changing vel
    else: # checking if snake on x-axis
        if key == 'a':
            movementData[1] = movementData[1]*(-1) # changing vel
    movementData[0] = not movementData[0] # changing axis

