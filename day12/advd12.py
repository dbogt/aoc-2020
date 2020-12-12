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
#%% Part 1 Functions
def newOrient(lastOrient, action, degrees):
    coord = ['N','E','S','W']
    rightDegrees = {'90':-3,'180':-2,'270':-1,'360':0}
    leftDegrees = {'90':-1,'180':-2,'270':-3,'360':-4} 
    idx = coord.index(lastOrient)
    if action == "L":
        turn = leftDegrees[str(degrees)]
    elif action == "R":
        turn = rightDegrees[str(degrees)]
    newDirect = coord[idx + turn]
    return newDirect

def shipMove(x0, y0, action, move, lastOrient):
#returns new x0, y0, and new orientation

    if action == "F":
        direct = lastOrient
    elif action == "L" or action == "R":
        direct = newOrient(lastOrient,action,move)
        return x0, y0, direct
    else:
        direct = action 
    
    if direct =="E":
        x0 += move
    elif direct=="W":
        x0 -= move
    elif direct =="N":
        y0 +=move
    elif direct =="S":
        y0 -= move
    
    return x0,y0,lastOrient

#%% Part 1 Solution
START_ORIENT = "E"
x = 0
y = 0
orient = START_ORIENT

moves = []

for command in commands:
    x, y, orient = shipMove(x, y, command['action'],command['val'],orient)
    moves.append([x,y,orient])
    
manhatDist = abs(moves[-1][0]) + abs(moves[-1][1])
print(manhatDist)

