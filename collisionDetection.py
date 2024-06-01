# this file is for collision detection

def collision_with_wall(breadth, height, headCoordinates):
    return not (0 < headCoordinates[0] < breadth+1 and 0 < headCoordinates[1] < height+1)
# if true, game ends, else continues

def collision_with_apple(headCoordinates, appleCoordinates):
    return headCoordinates == appleCoordinates
# if true, add 1 body part, else nothing

def collision_with_self(dictParts):
    return dictParts['O'] in dictParts['@']
# if true, game ends, else continues
