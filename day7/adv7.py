# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 08:49:17 2020

@author: Bogdan Tudose
"""
#%% Import packages
import numpy as np

#%% Source files
fPath = "day7/"
# f = open(fPath+"d7DemoInputs.txt", "r")
f = open(fPath+"d7ActualInputs.txt", "r")
inputs = f.read()
#%% Create Data Set
#Create a dictionary to store all bag info
#Format: {'parentBag':{'child1Bag':size, 'child2Bag':size}}

lines = [x for x in inputs.strip("\n").split("\n")]

bags = {}
for line in lines:
    splits = line.split(" bags contain ")
    parentBag = splits[0]
    childBags = splits[1].split(", ")
    dictBags = {}
    for child in childBags:
        print(child)
        text = child.replace(" bags","").replace(" bag","").replace(".","")
        print(text)
        if text[0:2] == "no":
            num = 0
            bagType = "None"
        else:
            num = int(text[0:2].replace(" ",""))
            bagType = text[2:]
        dictBags[bagType] = num
        
    # print(parentBag, childBags)
    bags[parentBag] = dictBags
#%% Part 1
allBags = []
firstSearch = "shiny gold"
    
searches = []
toSearch = [firstSearch]
found = []

while len(toSearch) != 0:
    search = toSearch[0]
    searches.append(search)
    print(search)
    for bagP, bagC in bags.items():
        if search in bagC.keys():
            if not(bagP in searches) and not(bagP in toSearch):
                toSearch.append(bagP)
                allBags.append(bagP)
    toSearch.remove(search)
    
allBags = list(set(allBags))
print(len(allBags))

#%% Part 2
pathCoeff = [1]
firstSearch = "shiny gold"
path = [firstSearch]
lastChildren = list(bags[firstSearch].keys())
allCoeff = [] #stores the number of bags needed as recursive function runs

def hasNoBags(bagType):
    return "None" in bags[bagType].keys()

def findNumBags(bagType, lastChildren):
    print("current path",path)
    if hasNoBags(bagType):
        print("no more bags")
        print(pathCoeff)
        print(np.product(pathCoeff))
        allCoeff.append(np.product(pathCoeff))
        print(path)
        pathCoeff.pop(len(pathCoeff)-1)
        path.pop(len(path)-1)
    else:
        lastChildren = list(bags[bagType].keys())
        for childBag, numBags in bags[bagType].items():
            print("going deeper")
            pathCoeff.append(numBags)
            path.append(childBag)
            findNumBags(childBag, lastChildren)
        print("done going through",bagType)
        print("adding another",bagType,np.product(pathCoeff))
        allCoeff.append(np.product(pathCoeff)) #parent bags needed
        pathCoeff.pop(len(pathCoeff)-1)
        path.pop(len(path)-1)

findNumBags("shiny gold",lastChildren)
print(np.sum(allCoeff)-1)