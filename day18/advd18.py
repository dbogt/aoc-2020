# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 00:07:12 2020

@author: Bogdan Tudose
"""

#%% Source files
fPath = "../aoc-2020-Src/"
# f = open(fPath+"d18DemoInputs.txt", "r")
f = open(fPath+"d18ActualInputs.txt", "r")
inputs = f.read()
lines = [x for x in inputs.strip("\n").split("\n")]

#%% Part 1 Functions
def evalGroup(parenthGroup):
    calc = 0
    lastOpp = "+"
    chars = parenthGroup.replace("(","").replace(")","").split(" ")
    for x in chars:
        if x == "+" or x == "*":
            lastOpp = x
        else:
            num = int(x)
            if lastOpp == "+":
                calc += num
            elif lastOpp == "*":
                calc *= num
    return calc
    
def findGroup(text):
    closeBracket = text.find(")")
    for x in range(closeBracket,-1,-1):
        if text[x] == "(":
            openBracket = x
            break
    
    group = text[openBracket:closeBracket+1]
    print(group)
    return group

#%% Part 1
results = []
for line in lines:
    currLine = line
    while currLine.find(")") >= 0:
        print(currLine)
        result = findGroup(currLine)
        currLine = currLine.replace(result,str(evalGroup(result)))
    
    results.append(evalGroup(currLine))

print(sum(results))