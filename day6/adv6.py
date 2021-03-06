# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 00:08:29 2020

@author: Bogdan Tudose
"""
#%% Source files
fPath = "../aoc-2020-Src/"
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
    counts.append(len(answers))
    
print(np.sum(counts))
#%% Part 2
groups = [x for x in inputs.strip("\n").split("\n\n")]

counts = []
for group in groups:
    groupSize = len(group.split("\n"))
    answers = [x for x in group.replace("\n","")]
    uniqueAnswers = set(answers)
    allAnswered = 0
    for ans in uniqueAnswers:
        if answers.count(ans) == groupSize:
            allAnswered += 1
    counts.append(allAnswered)
    
print(np.sum(counts))