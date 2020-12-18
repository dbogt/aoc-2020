# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 00:37:53 2020

@author: Bogdan Tudose
"""

#%% Packages
import math
#%% Source files
fPath = "../aoc-2020-Src/"
# f = open(fPath+"d18DemoInputs.txt", "r")
f = open(fPath+"d18ActualInputs.txt", "r")
inputs = f.read()
lines = [x for x in inputs.strip("\n").split("\n")]

#%% Part 2 Functions
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
    return group

def part2EvalGroup(parenthGroup):
    groups = parenthGroup.replace("(","").replace(")","").split(" * ")
    added= []
    for addGroup in groups:
        evaluated = evalGroup(addGroup)
        added.append(evaluated)
        
    prod = math.prod(added)
    return prod
#%% Part 1
results = []
for line in lines:
    currLine = line
    while currLine.find(")") >= 0:
        print(currLine)
        result = findGroup(currLine)
        currLine = currLine.replace(result,str(evalGroup(result)))
    
    results.append(evalGroup(currLine))

print("Part 1",sum(results))

#%% Part 2
results = []
for line in lines:
    currLine = line
    while currLine.find(")") >= 0:
        print(currLine)
        bracketGroup = findGroup(currLine)
        #calculated + before * in bracket group
        currLine = currLine.replace(bracketGroup,str(part2EvalGroup(bracketGroup)))
    
    results.append(part2EvalGroup(currLine))       
print("Part 2",sum(results))