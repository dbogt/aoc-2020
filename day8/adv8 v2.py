# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 08:49:17 2020

@author: Bogdan Tudose
"""
#%% Import packages
import pandas as pd

#%% Source files
fPath = "day8/"
# f = open(fPath+"d8DemoInputs.txt", "r")
f = open(fPath+"d8ActualInputs.txt", "r")
inputs = f.read()

#%% Create Data Set
codes = [x for x in inputs.strip("\n").split("\n")]

def createCodes():
    cleanCodes = []
    for code in codes:
        splits = code.split(" ")
        command = splits[0]
        value = int(splits[1])
        dictCode = {"code":command,"value":value,"hasRun":0}
        cleanCodes.append(dictCode)
    return cleanCodes

#%% Part 1
dictCodes = createCodes()

stopInfLoop = 0
lineRun = 0
accVal = 0
while stopInfLoop == 0:
# for x in range(100):
    if dictCodes[lineRun]['hasRun'] == 1:
        stopInfLoop = 1
        break
    print("running", lineRun, dictCodes[lineRun])

    code = dictCodes[lineRun]['code']
    val = dictCodes[lineRun]['value']
    dictCodes[lineRun]['hasRun'] = 1
    
    if code == "nop":
        lineRun +=1
    elif code == "acc":
        accVal += val
        lineRun +=1
    elif code == "jmp":
        lineRun += val
    
print(accVal)
#%% Part 2
dictCodes = createCodes()

df = pd.DataFrame(dictCodes)    

nops = df[df['code']=='nop']    
jmps = df[df['code']=='jmp']    
nopsLines = list(nops.index) 
jmpsLines = list(jmps.index)

checkLines = jmpsLines + nopsLines

#%% Function to reset the "hasRun" key in dictionaries
def resetHasRun(codes):
    for code in codes:
        code['hasRun'] = 0
#%% Part 2
dictCodes = createCodes()
foundFix = 0
for checkLine in checkLines:
    if foundFix == 1:
        break
    oldCode = dictCodes[checkLine]['code']
    if oldCode == "jmp":
        newCode = "nop"
    elif oldCode == "nop":
        newCode = "jmp"
    print("changing line",checkLine,"from",oldCode,"to",newCode)
    dictCodes[checkLine]['code'] = newCode
    stopInfLoop = 0
    lineRun = 0
    accVal = 0

    while stopInfLoop == 0 and foundFix == 0:
        if dictCodes[lineRun]['hasRun'] == 1:
            stopInfLoop = 1
            print("not fixed", accVal)
            dictCodes[checkLine]['code'] = oldCode
            break
        code = dictCodes[lineRun]['code']
        val = dictCodes[lineRun]['value']
        dictCodes[lineRun]['hasRun'] = 1
        
        if code == "nop":
            lineRun +=1
        elif code == "acc":
            accVal += val
            lineRun +=1
        elif code == "jmp":
            lineRun += val
        if lineRun == len(codes):
            print("fixed, acc value is ", accVal)
            foundFix = 1
            # dictCodes[checkLine]['code'] = 'nop'
            print(checkLine, dictCodes[checkLine])
            # break
    resetHasRun(dictCodes)
    
# dictCodes[313]['code'] = 'jmp'