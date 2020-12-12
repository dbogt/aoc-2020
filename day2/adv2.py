# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 01:45:32 2020

@author: Bogdan Tudose
"""

#%% Source files
fPath = "../aoc-2020-Src/"
f = open(fPath+"d2ActualInputs.txt", "r")
inputs = f.read()

#%%
import pandas as pd
#%%
codes = [x.split(" ") for x in inputs.strip("\n").split("\n")]

dataBase = []
dictCodes = {}
for x in codes:
    rule = x[0]
    letter = x[1].replace(":","")
    password = x[2]
    countLett = password.count(letter)
    obj = {"rule":rule,
           "letter":letter,
           "pass":password,
           "min":int(rule.split("-")[0]),
           "max":int(rule.split("-")[1]),
           "count":countLett}
    dataBase.append(obj)


df = pd.DataFrame(dataBase)
df['IsValid'] = (df['count'] >= df['min']) & (df['count'] <= df['max']) 

df[df['IsValid']]

#%% Part 2
dataBase = []
dictCodes = {}
for x in codes:
    rule = x[0]
    letter = x[1].replace(":","")
    password = x[2]
    occur1 = int(rule.split("-")[0])
    occur2 = int(rule.split("-")[1])
    occLet1 = password[occur1 - 1]
    occLet2 = password[occur2 - 1]
    obj = {"rule":rule,
           "letter":letter,
           "pass":password,
           "occur1":occur1,
           "occur2":occur2,
           "let1":occLet1,
           "let2":occLet2}
    dataBase.append(obj)
df = pd.DataFrame(dataBase)
df['Both Occur'] = (df['let1'] == df['letter']) & (df['let2'] == df['letter'])
df['At Least One Occurs'] = (df['let1'] == df['letter']) | (df['let2'] == df['letter'])
df['Is Valid'] = (df['Both Occur']==False) & (df['At Least One Occurs']==True)

validPasswords = df[df['Is Valid']]
