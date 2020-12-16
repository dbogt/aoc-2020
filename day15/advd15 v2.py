# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 01:52:09 2020

@author: Bogdan Tudose
"""

#%% Part 1
# nums = [0,3,6] #demo
nums = [1,0,15,2,10,13] #actual input

prevSpoken = {}
sequence = []

for idx, x in enumerate(nums):
    prevSpoken[x] = []
    prevSpoken[x].append(idx + 1)
    sequence.append(x)

#%%
# sequence = [0,3,6,0,3]
lastNum = nums[-1]

def addLastSpoken(x, newidx):
    if x in prevSpoken.keys():
        if len(prevSpoken[x]) > 1:
            prevSpoken[x][-2] = prevSpoken[x][-1]
            prevSpoken[x][-1] = newidx
        else:
            prevSpoken[x].append(newidx)
    else:
        prevSpoken[x] = []
        prevSpoken[x].append(newidx)
#%%
for idx in range(len(nums)+1, 30000001):
    # print(idx)
    if (idx % 1000000) == 0:
        print(idx)
    if len(prevSpoken[lastNum]) == 1:
        lastNum = 0
        addLastSpoken(lastNum, idx)
    else:
        diff = prevSpoken[lastNum][-1] - prevSpoken[lastNum][-2]
        lastNum = diff
        addLastSpoken(diff, idx)
            
print("Part 1:",lastNum)
