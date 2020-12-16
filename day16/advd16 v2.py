# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 23:59:18 2020

@author: Bogdan Tudose
"""
#%% Packages
import pandas as pd

#%% Source files
fPath = "../aoc-2020-Src/"
# f = open(fPath+"d16DemoInputs.txt", "r")
f = open(fPath+"d16ActualInputs.txt", "r")
inputs = f.read()
lines = [x for x in inputs.strip("\n").split("\n")]

#%% Parsing Text Input
splits = inputs.split("nearby tickets:\n")
nearbyTickets = [y.split(",") for y in [x for x in splits[1].split("\n")] ]
myTix = [int(x) for x in splits[0].split("your ticket:")[1].strip("\n").split(",")]

#Creating the rules dictionary
rulesLines = [x for x in splits[0].split("your ticket:")[0].strip("\n").split("\n")]
rulesDict = {}
for rule in rulesLines:
    ruleSplit = rule.split(": ")
    ruleType = ruleSplit[0]
    ranges = ruleSplit[1].split(" or ")
    range1 = [int(x) for x in ranges[0].split("-")]
    range2 = [int(x) for x in ranges[1].split("-")]
    range1Nums = [x for x in range(range1[0],range1[1] +1)]
    range2Nums = [x for x in range(range2[0],range2[1] +1)]
    rulesDict[ruleType] = range1Nums + range2Nums

allNums = []
for nums in rulesDict.values():
    allNums.extend(nums)

allNums = list(set(allNums))
#%% Part 1 - Check nearby tickets
invalidValues = []
checkValidTix = {}
for idx, tix in enumerate(nearbyTickets):
    countInvalid = 0
    for num in tix:
        val = int(num)
        if val not in allNums:
            invalidValues.append(val)
            countInvalid += 1
    if countInvalid > 0:
        checkValidTix[idx] = "not valid"
    else:
        checkValidTix[idx] = "valid"
            
print(sum(invalidValues))
#%% Part 2
#Using Pandas for a quick filter of valid tickets
df = pd.DataFrame(nearbyTickets)
df['IsValid'] = checkValidTix.values()

validTix = df[df['IsValid'] == 'valid'] #filter

#Extract each column from all nearby valid tickets in seperate lists
cols = []
for colNum in range(0,20):
    nums = list(validTix[colNum].unique().astype(int))
    nums.sort()
    cols.append(nums)

#%% Rules Matrix
#determine which columns are valid for which rules
rulesPossible = {}
for ruleType, ruleRange in rulesDict.items():
    validCols = []
    for idx, col in enumerate(cols):
        for x in col:
            if x not in ruleRange:
                break #column does not meet criteria for rule
        else:
            validCols.append(idx)
            continue
            
    rulesPossible[ruleType] = validCols.copy()
            
#%% Final Dictionary
finalMap = {}
#Find Unique Column for Each Rule
for ruleNum in range(20):
    for ruleType, possCols in rulesPossible.items():
        if len(possCols) == 1:
            onlyCol = possCols[0]
            # ruleFound = ruleType
            finalMap[ruleType] = rulesPossible.pop(ruleType,None)
            break
    #Delete unique value
    for ruleType, possCols in rulesPossible.items():
        possCols.remove(onlyCol)

#%% My Ticket Nums
foundMapDF = pd.DataFrame(finalMap).T
departColsDF = foundMapDF[foundMapDF.index.str.contains("departure")]
depFields = list(departColsDF[0])

depNums = [myTix[x] for x in depFields]
departColsDF['My Ticket'] = depNums
print("Part 2 Answer:", departColsDF['My Ticket'].product())
