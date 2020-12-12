# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:24:01 2020

@author: Bogdan Tudose
"""

#%% Source files
fPath = "../aoc-2020-Src/"
f = open(fPath+"d1ActualInputs.txt", "r")
inputs = f.read()
#%% Part 1
nums = [int(x) for x in inputs.strip("\n").split("\n")]

for num in nums:
    print(num)
    for num2 in nums:
        if num + num2 == 2020:
            print(num, num2, num * num2)
            break
    else:
        continue
    break

#%% Part 2
for num in nums:
    print(num)
    for num2 in nums:
        for num3 in nums:
            if num + num2 + num3 == 2020:
                print(num, num2, num3, num + num2+ num3, num * num2 * num3)
                break
    else:
        continue
    break
