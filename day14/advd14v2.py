# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 00:11:32 2020

@author: Bogdan Tudose
"""
#%% Import packages
import itertools
#%% Source files
fPath = "../aoc-2020-Src/"
# f = open(fPath+"d14DemoInputs.txt", "r")
# f = open(fPath+"d14DemoInputsP2.txt", "r")

f = open(fPath+"d14ActualInputs.txt", "r")
inputs = f.read()
lines = [x for x in inputs.strip("\n").split("\n")]
#%% Part 1
currMask = ""
memories = {}

for line in lines:
    if line.find("mask") >= 0:
        currMask = line.replace("mask = ","")
    elif line.find("mem") >= 0:
        memoryCommand = line.split(" = ")
        mem = int(memoryCommand[0].replace("mem[","").replace("]",""))
        decNum = int(memoryCommand[1])
        binNum = bin(decNum).replace("0b","")
        binNum36 = "0" * (36 - len(binNum)) + binNum
        newBin = ""
        for idx, bit in enumerate(binNum36):
            if currMask[idx] == "X":
                newBin += bit
            else:
                newBin += currMask[idx] 
        newDec = int(newBin,2)
        memories[mem] = newDec
        
nums = list(memories.values())
print("Answer to part 1:",sum(nums))
#%% Part 2
def binseq(k):
    return [''.join(x) for x in itertools.product('01', repeat=k)]

currMask = ""
memories = {}

for line in lines:
    if line.find("mask") >= 0:
        currMask = line.replace("mask = ","")
    elif line.find("mem") >= 0:
        memoryCommand = line.split(" = ")
        mem = int(memoryCommand[0].replace("mem[","").replace("]",""))
        val = int(memoryCommand[1])
        binNum = bin(mem).replace("0b","")
        binNum36 = "0" * (36 - len(binNum)) + binNum
        floatBin = ""
        for idx, bit in enumerate(binNum36):
            if currMask[idx] == "0":
                floatBin += bit
            elif currMask[idx] == "1" or currMask[idx] == "X":
                floatBin += currMask[idx]
        
        countX = floatBin.count('X')
        xPerm = binseq(countX)
        for perm in xPerm:
            newBin = floatBin
            for pos in range(len(perm)):        
                newBin = newBin.replace("X",perm[pos],1)
            memories[newBin] =val

nums = list(memories.values())
print("Answer to part 2:",sum(nums))