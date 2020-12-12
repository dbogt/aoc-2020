# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 00:00:39 2020

@author: Bogdan Tudose
"""
#%% Import packages
import numpy as np

#%% Source files
fPath = "../aoc-2020-Src/"
# f = open(fPath+"d10DemoInputs.txt", "r")
f = open(fPath+"d10ActualInputs.txt", "r")
inputs = f.read()

adapters = [int(x) for x in inputs.strip("\n").split("\n")]
adapters.sort()

#%% Part 1

outlet = 0
currentJolt = outlet

deviceJolt = adapters[-1] + 3 #max adapter jolt + 3

diff1s = 0
diff2s = 0
diff3s = 1 #device already has jolt diff of 3
diffs = []
for adapt in adapters:
    diff = adapt - currentJolt
    diffs.append(diff)
    if diff == 1:
        diff1s += 1
    elif diff == 2:
        diff2s += 1
    elif diff == 3:
        diff3s += 1
    else:
        print(adapt, "is > 3 jolt diff")
        break
    currentJolt = adapt

print("Answer part 1:",diff1s * diff3s)

#%% Part 2
#using differences to determine # of branches for each group of consecutive #s
    #then multiple the # of branches in each chunck of cons #s
splits = "".join([str(x) for x in diffs]).split("3")
multipliers = []
for x in splits:
    if x =="11": #three consecutive numbers
        multipliers.append(2)
    elif x == "111": #four consec numbers
        multipliers.append(4)
    elif x == "1111": #five consec numb
        multipliers.append(7)
    else: #no consec numbers
        multipliers.append(1)

import pandas as pd
df = pd.DataFrame({"mult":multipliers})
df['mult'].product()

#%% Part 2 - Solution 2
# #%% Part 2
tree = {}

for x in adapters:
    nextAvail = []
    for diff in range(1,4):
        if (x + diff) in adapters:
            nextAvail.append(x+diff)
    tree[x] = nextAvail


# perms = []
# for x in tree.values():
#     print(len(x))
#     perms.append(len(x))
#%%

    
# from functools import lru_cache

# iterCount = 0

# # # @lru_cache
# # @lru_cache
def joltRecursion(adapt):
    global iterCount
    if adapt == adapters[-1]: #last adapter
        iterCount += 1
        return 1
    count = 0
    for diff in range(1,4):
        
        if (adapt + diff) in adapters:
           count += joltRecursion(adapt + diff)Answer
       return count

x =  joltRecursion(0)

# # #%%
# # counter = 0
# # q = [0]

# # while len(q) != 0:
# #     if q[0] == adapters[-1]:
# #         counter +=1
# #     if q[0] + 1 in adapters:
# #         q += [q[0] + 1]
# #     if q[0] + 2 in adapters:
# #         q += [q[0] + 2]
# #     if q[0] + 3 in adapters:
# #         q += [q[0] + 3]
# #     del q[0]

# # #%%
# # w = []
# # def ways(lines,i):
# #     global w
# #     if w[i] != -1:
# #         return w[i]
# #     if i == len(lines) - 1:
# #         return 1
# #     ans = 0
# #     for j in range(i+1,len(lines)):
# #         if lines[j] - lines[i] < 4:
# #             ans += ways(lines,j)
# #     w[i] = ans
# #     return ans

# # w = [-1 for _ in range(len(adapters))]
# # print(ways(adapters,0))
