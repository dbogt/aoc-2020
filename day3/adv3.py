# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 02:18:07 2020

@author: Bogdan Tudose
"""

fPath = r"C:\Users\bogda\Desktop\Python\Challenge\2020"
f = open(fPath+"\d3ActualInputs.txt", "r")
inputsActual = f.read()

#%% Load Data
# inputs = inputsDemo
inputs=inputsActual
lines = [x for x in inputs.strip("\n").split("\n")]

#%%Functions used
def replaceTextIndex(text, idx, newChar):
    newText = text[0:idx] + newChar + text[idx+1:]
    return newText

#%% Generic Function
def part1(xDist,yDist):
    numLines = len(lines)
    currCols = len(lines[0])
    minCols = 1 + xDist * (numLines * yDist -1)
    timesRepeat = int (minCols / currCols) + 1
    
    linesRepeated = [x * timesRepeat for x in lines]
    mapLines = "\n".join(linesRepeated)
    
    newMap = linesRepeated.copy()
    movesDown = 1
    for lineNum in range(yDist, len(linesRepeated), yDist):
        sledPosX = movesDown * xDist
        sledPosY = lineNum
        isTree = linesRepeated[lineNum][sledPosX] == "#"
        if isTree:
            newC = "X"
        else:
            newC = "O"
        newMap[lineNum] = replaceTextIndex(linesRepeated[sledPosY],sledPosX,newC)
        movesDown +=1
    
    newMapOutput = "\n".join(newMap)
    
    treesHit = newMapOutput.count("X")
    return treesHit, mapLines, newMapOutput

#%% Part 1
x = 3
y = 1 
trees, oldMap, newMap = part1(x,y)
print(trees)
#%% Part 2
xVals = [1, 3, 5, 7, 1]
yVals = [1, 1, 1, 1, 2]
treesHit = []
maps = []
for idx, x in enumerate(xVals):
    hits, oldMap, newMap = part1(x, yVals[idx])
    treesHit.append(hits)
    maps.append(newMap)

import math
math.prod(treesHit)
