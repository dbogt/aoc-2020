# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 00:08:40 2020

@author: Bogdan Tudose
"""

#%% Source files
fPath = "../aoc-2020-Src/"
# f = open(fPath+"d12DemoInputs.txt", "r")
f = open(fPath+"d12ActualInputs.txt", "r")
inputs = f.read()

lines = [x for x in inputs.strip("\n").split("\n")]

commands = []
for line in lines:
    action = line[0]
    val = int(line[1:])
    commands.append({"action":action, "val":val})
#%% Part 2 Functions
def rotateWaypoint(action, degrees, xWay, yWay):
    coord = ['N','E','S','W']
    rightDegrees = {'90':-3,'180':-2,'270':-1,'360':0}
    leftDegrees = {'90':-1,'180':-2,'270':-3,'360':-4} 
    
    if xWay >= 0:
        wayDir1 = "E"
    else:
        wayDir1 = "W"
    
    if yWay >= 0:
        wayDir2 = "N"
    else:
        wayDir2 = "S"

    idx1, idx2 = coord.index(wayDir1), coord.index(wayDir2)
    if action == "L":
        turn = leftDegrees[str(degrees)]
    elif action == "R":
        turn = rightDegrees[str(degrees)]
    newWayDir1, newWayDir2 = coord[idx1 + turn], coord[idx2 + turn]

    wayPointCoords = {}
    wayPointCoords[newWayDir1] = abs(xWay)
    wayPointCoords[newWayDir2] = abs(yWay)
    
    for key, val in wayPointCoords.items():
        if key == 'W':
            newXWay = val * -1
        elif key == "E":
            newXWay = val
        elif key == "N":
            newYWay = val
        elif key == "S":
            newYWay = val * -1            

    return newXWay, newYWay

def wayPtMove(x0, y0, action, move):
#returns new x0, y0, and new orientation
    if action == "L" or action == "R":
        newX, newY = rotateWaypoint(action, move, x0, y0)
        return newX, newY
    
    if action =="E":
        x0 += move
    elif action =="W":
        x0 -= move
    elif action =="N":
        y0 +=move
    elif action =="S":
        y0 -= move
    
    return x0,y0

#%% Part 2 Solution
xW, yW = 10, 1 #waypoint coord
x, y = 0, 0 #ship coord

orient = START_ORIENT

moves = []

for command in commands:
    action = command['action']
    value = command['val']
    if action == "F":
        #move ship towards waypoint
        x += xW * value
        y += yW * value
        
    else:
        #move or re-orient the waypoint
        xW, yW = wayPtMove(xW, yW, action, value)
    moves.append({'ship':[x,y],'waypoint':[xW,yW]})
    
manhatDist = abs(moves[-1]['ship'][0]) + abs(moves[-1]['ship'][1])
print(manhatDist)

