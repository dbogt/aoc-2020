# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 23:52:19 2020

@author: Bogdan Tudose
"""
#%% Import packages
import numpy as np

#%% Source files
fPath = "day9/"
# f = open(fPath+"d9DemoInputs.txt", "r")
f = open(fPath+"d9ActualInputs.txt", "r")
inputs = f.read()

#%% Create Data Set
nums = [int(x) for x in inputs.strip("\n").split("\n")]

#%% Part 1
preamble = 25
for idx in range(preamble,len(nums)):
    subset = nums[idx-preamble:idx]
    checkNum = nums[idx]
    for x in subset:
        diff = checkNum - x
        if (diff in subset) and (diff != x):
            break
    else:
        invalidNum = checkNum
        print(checkNum,"has no match")
        break
#%% Part 2
for idx, x in enumerate(nums):
    sumNums = x #start with sum = to first number in contig range
    addIdx = idx + 1
    while sumNums < invalidNum:
        sumNums += nums[addIdx]
        addIdx += 1
    if sumNums == invalidNum:
        foundSubset = nums[idx:addIdx].copy()
        break

print("contig subset:", foundSubset)
print("encryption weakness:",np.max(foundSubset) + np.min(foundSubset))