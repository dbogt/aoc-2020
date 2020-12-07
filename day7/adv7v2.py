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
    #Text cleaning
    splits = line.split(" bags contain ") #split between parent bag and children bags
    parentBag = splits[0]
    childBags = splits[1].split(", ")
    dictBags = {}
    for child in childBags:
        text = child.replace(" bags","").replace(" bag","").replace(".","")
        if text[0:2] == "no":
            num = 0
            bagType = "None"
        else:
            num = int(text[0:2].replace(" ",""))
            bagType = text[2:]
        dictBags[bagType] = num
        
    bags[parentBag] = dictBags
#%% Part 1
allBags = []
firstSearch = "shiny gold"
    
searches = []
toSearch = [firstSearch]

while len(toSearch) != 0:
    search = toSearch[0]
    searches.append(search)
    for bagP, bagC in bags.items():
        if search in bagC.keys():
            if not(bagP in searches) and not(bagP in toSearch):
                toSearch.append(bagP)
                allBags.append(bagP)
    toSearch.remove(search)
    
allBags = list(set(allBags))
print(len(allBags))

#%% Part 2
pathCoeff = [1] #start off with # of shiny gold bags needed
firstSearch = "shiny gold"
path = [firstSearch]
allCoeff = [] #stores the number of bags needed as recursive function runs

def findNumBags(bagType):
    numBags = np.product(pathCoeff)
    # print(path, numBags, pathCoeff) #uncomment to see Tree
    allCoeff.append(numBags)
    if "None" in bags[bagType].keys(): #no more bags to check in this path
        pathCoeff.pop(len(pathCoeff)-1)
        path.pop(len(path)-1)
    else: #go deeper        
        for childBag, numBags in bags[bagType].items():
            pathCoeff.append(numBags)
            path.append(childBag)
            findNumBags(childBag)
        pathCoeff.pop(len(pathCoeff)-1)
        path.pop(len(path)-1)

findNumBags(firstSearch)
print("Total Bags Needed:",np.sum(allCoeff)-1)