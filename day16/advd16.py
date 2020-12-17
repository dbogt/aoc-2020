# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 23:59:18 2020

@author: Bogdan Tudose
"""
#%% Source files
fPath = "../aoc-2020-Src/"
# f = open(fPath+"d16DemoInputs.txt", "r")

f = open(fPath+"d16ActualInputs.txt", "r")
inputs = f.read()
lines = [x for x in inputs.strip("\n").split("\n")]


#%% Creating Data
splits = inputs.split("nearby tickets:\n")
nearbyLines = [x for x in splits[1].split("\n")]
nearbyTickets2 = [ x for x in splits[1].split("\n") ]
nearbyTickets = [x.split(",") for x in nearbyLines]

nearbyValid = {}
rulesText = splits[0].split("your ticket:")[0]
rules = [x for x in rulesText.strip("\n").split("\n")]
rulesDict = {}
for rule in rules:
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


#%% Check nearby tickets
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
#%%
import pandas as pd
df = pd.DataFrame(nearbyTickets)

df['IsValid'] = checkValidTix.values()

validTix = df[df['IsValid'] == 'valid']
stats = validTix.describe()

cols = []
for colNum in range(0,20):
    nums = list(validTix[colNum])
    nums = [int(x) for x in nums]
    nums.sort()
    nums = list(set(nums))
    cols.append(nums)

#%% Rules Matrix
rulesPossible = {}
for ruleType, ruleRange in rulesDict.items():
    validCols = []
    print(ruleType)
    for idx, col in enumerate(cols):
        for x in col:
            if x not in ruleRange:
                print(x, "in col ",idx,"no bueno for",ruleType)
                break
        else:
            validCols.append(idx)
            continue
            
    rulesPossible[ruleType] = validCols.copy()

#%%
'arrival track: 30-630 or 647-957'
notValid = [x for x in range(631,647)]
for idx, col in enumerate(cols):
    print("checking col",idx)
    for x in col:
        if x in notValid:
            print("no bueno, found", x)
            break
    else:
        continue
            
#%% Final Dictionary
finalMap = {}
#Find Unique value
#%%
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
myTix = [157,101,107,179,181,163,191,109,97,103,89,113,167,127,151,53,83,61,59,173]

foundMapDF = pd.DataFrame(finalMap).T
depCols = foundMapDF[foundMapDF.index.str.contains("departure")]
depFields = list(depCols[0])

depNums = [myTix[x] for x in depFields]

product = 1
for x in depNums:
    product *= x
