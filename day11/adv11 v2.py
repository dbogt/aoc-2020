# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 00:09:47 2020

@author: Bogdan Tudose
"""

#%%
import copy

#%% Source files
fPath = "../aoc-2020-Src/"
# f = open(fPath+"d11DemoInputs.txt", "r")
f = open(fPath+"d11ActualInputs.txt", "r")
inputs = f.read()

#%%
lines = [x for x in inputs.strip("\n").split("\n")]

#add padding to make checking corners and edges easier
lines = ["." + i + "." for i in lines]
lines = ["." * len(lines[0])] + lines + ["." * len(lines[0])]
#%%
seats = []

for line in lines:
    row = [x for x in line]
    seats.append(row)

maxCol = len(seats[0]) - 1
maxRow = len(seats) - 1

#%% 
#(dx,dy) --> change in col, change in row
coords = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        #topleft, topmid, topright, left, right, botleft, botmid, botright
#%% Part 1 Function
def findOccupied(rowN, colN, seatsList):
    currStatus = seatsList[rowN][colN]
    countOcc = 0
    
    #check if any surr seats are occupied
    for x,y in coords:
        if seatsList[rowN + y][colN + x] == "#":
            if currStatus == "L":
                return "L" #all seats around L need to be empty to change to occupied
            elif currStatus == "#":
                countOcc += 1
                if countOcc >= 4:
                    return "L"
        
    return "#" #if no occupied seats, L becomes occupied

#%% Part 1 Solution
changedStates = []
changeState = -1

while changeState != 0:
    newSeats = copy.deepcopy(seats)
    changeState = 0
    for row in range(0,maxRow+1):
        for col in range(0, maxCol+1):
            typeArea = seats[row][col]
            if typeArea != ".":
                new = findOccupied(row,col,seats)
                if typeArea != new:
                    changeState +=1
                newSeats[row][col] = new
    changedStates.append(changeState)
    seats=copy.deepcopy(newSeats)
    if changeState == 0:
        mapOutput = ["".join(x) for x in newSeats]
        mapOutput = '\n'.join(mapOutput) 
        print(mapOutput.count("#"))


#%% Part 2 Function
def findOccupiedVisible(rowN, colN, seatsList):
    currStatus = seatsList[rowN][colN]
    countOcc = 0
    #check if any surr seats are occupied
    # print("x"*20)
    for x,y in coords:
        # print("-"*20)
        # print("direction is now ", x, y)
        currRow, currCol = rowN, colN
        
        findingSeat = True        
        while findingSeat:
            currRow += y
            currCol += x
            # print(currCol,currRow)
            if (currRow < 0 or currRow > maxRow) or (currCol < 0 or currCol > maxCol):
                # print("off the map")
                findingSeat = False #reached end of visiability
                break
            if seatsList[currRow][currCol] == "#":
                # print("found #")
                if currStatus == "L":
                    return "L" #all seats around L need to be empty to change to occupied
                elif currStatus == "#":
                    countOcc += 1
                    findingSeat = False
                    
                    if countOcc >= 5:
                        return "L"
                    break
            elif seatsList[currRow][currCol] == "L":
                findingSeat = False #found empty seat, try another direction
                break
        
    return "#" #if no occupied seats, L becomes occupied


#%% Part 2 Solution
changedStates = []

changeState = -1
iters = 0

while changeState != 0:
# while iters < 1:
    newSeats = copy.deepcopy(seats)
    changeState = 0
    for row in range(0,maxRow+1):
        for col in range(0, maxCol+1):
            # print("now looking at",row,col)
            typeArea = seats[row][col]
            if typeArea != ".":
                new = findOccupiedVisible(row,col,seats)
                # print("location ",row, col,"changed to",new)
                if typeArea != new:
                    changeState +=1
                newSeats[row][col] = new
    changedStates.append(changeState)
    seats=copy.deepcopy(newSeats)
    if changeState == 0:
        mapOutput = ["".join(x) for x in newSeats]
        mapOutput = '\n'.join(mapOutput) 
        print(mapOutput.count("#"))
    iters +=1    