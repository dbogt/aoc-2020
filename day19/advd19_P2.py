# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 23:59:15 2020

@author: Bogdan Tudose
"""
#%% Packages
import re
#%% Source files
fPath = "../aoc-2020-Src/"
# f = open(fPath+"d19DemoInputs.txt", "r")
f = open(fPath+"d19ActualInputs.txt", "r")
inputs = f.read()

splits = inputs.split("\n\n")
rules = splits[0]
msgs = [x for x in splits[1].strip("\n").split("\n")]

#%% Create Rules Dictionary
ruleLines = [x for x in rules.strip("\n").split("\n")]

rulesDict = {}
test = ruleLines[0]
test.find(":")
references = []
for line in ruleLines:
    ruleCode = line.split(": ")[0]
    rule = line.split(": ")[1]
    if rule == '"a"':
        codeA = ruleCode
    elif rule == '"b"':
        codeB = ruleCode
        
    otherCodes = rule.replace(" | "," ").split(" ")
    references.extend(otherCodes)
    rulesDict[ruleCode] = rule

#%% Part 1 Function
rules = rulesDict.copy()
cleanRules = {}

def createRegex(codeID):
    #prevent rerunning already found regex
    if codeID in cleanRules.keys(): 
        return cleanRules[codeID]
    if codeID == codeA:
        return "a"
    elif codeID == codeB:
        return "b"
    
    #new regex
    #https://regex101.com/
    #Note: regex (a|b)b is the same as ab | bb
    groupWrapper = "({})"
    
    regex = ["|" if code=="|" else createRegex(code) for code in rules[codeID].split()]

    groupedRegex = groupWrapper.format("".join(regex))
    cleanRules[codeID] = groupedRegex
    return groupedRegex
    

def createRegexP2(codeID, selfLoop, maxLoops):
    if selfLoop == maxLoops:
        return ""
    #prevent rerunning already found regex
    if codeID in cleanRules.keys(): 
        return cleanRules[codeID]
    if codeID == codeA:
        return "a"
    elif codeID == codeB:
        return "b"
    
    #new regex
    #https://regex101.com/
    #Note: regex (a|b)b is the same as ab | bb
    groupWrapper = "({})"
    
    regex = ["|" if code=="|" else createRegexP2(code, selfLoop+1,maxLoops) if code == codeID
             else createRegexP2(code, 0,maxLoops) for code in rules[codeID].split()]

    groupedRegex = groupWrapper.format("".join(regex))
    cleanRules[codeID] = groupedRegex
    return groupedRegex
#%% Part 1
cleanRules = {}
allRegex = createRegex("0")

validCounts = 0
for msg in msgs:
    if re.fullmatch(allRegex, msg):
        validCounts += 1

print("Part 1 answer:",validCounts)

#%% Part 2
rules = rulesDict.copy()
rules["8"] = "42 | 42 8"
rules["11"] = "42 31 | 42 11 31"

part2Answers = []
sameResult = 0

for maxLoops in range(0,20):
    cleanRules = {}
    allRegex = createRegexP2("0",0,maxLoops)
    
    validCounts = 0
    for msg in msgs:
        if re.fullmatch(allRegex, msg):
            validCounts += 1
    
    part2Answers.append(validCounts)
    print("Part 2 answer:",validCounts)
    if len(part2Answers) > 1: 
        if part2Answers[-1] == part2Answers[-2]:
            sameResult += 1

    #if still getting the same result after 5 deeper loops stop
    if sameResult == 5: 
        break
    
