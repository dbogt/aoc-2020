# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 00:08:29 2020

@author: Bogdan Tudose
"""

#%% Source files
fPath = "day6/"
# f = open(fPath+"d6DemoInputs.txt", "r")
f = open(fPath+"d6ActualInputs.txt", "r")

inputs = f.read()

#%% Import package
import numpy as np
#%% Part 1
groups = [x for x in inputs.strip("\n").split("\n\n")]

counts = []
for group in groups:
    answers = [x for x in group.replace("\n","")]
    answers = set(answers)
    print(len(answers))
    counts.append(len(answers))
    
print(np.sum(counts))

#%% Part 2
groups = [x for x in inputs.strip("\n").split("\n\n")]
groupSizes = [len(x.split("\n")) for x in groups]

counts = []
for group in groups:
    groupSize = len(group.split("\n"))
    answers = [x for x in group.replace("\n","")]
    uniqueAnswers = set(answers)
    allAnswered = 0
    for x in uniqueAnswers:
        if answers.count(x) == groupSize:
            allAnswered += 1
        
    print(allAnswered)
    counts.append(allAnswered)
    
print(np.sum(counts))