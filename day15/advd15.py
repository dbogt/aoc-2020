# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 01:52:09 2020

@author: Bogdan Tudose
"""


#%% Part 1
nums = [0,3,6] #demo
# nums = [1,0,15,2,10,13] #actual input



prevSpoken = {}
sequence = []

for idx, x in enumerate(nums):
    prevSpoken[x] = []
    prevSpoken[x].append(idx + 1)
    sequence.append(x)



#%%
# sequence = [0,3,6,0,3]

for idx in range(len(nums)+1, 30000000):
    lastNum = sequence[-1]
    # if lastNum in prevSpoken.keys():
    if len(prevSpoken[lastNum]) == 1:
        #spoken only once, say 0
        currNum = 0
        sequence.append(currNum)
        prevSpoken[currNum].append(idx)
    else:
        diff = prevSpoken[lastNum][-1] - prevSpoken[lastNum][-2]
        sequence.append(diff)
        if diff in prevSpoken.keys():
            prevSpoken[diff].append(idx)
        else:
            prevSpoken[diff] = []
            prevSpoken[diff].append(idx)
            
print("Part 1:",sequence[-1])
