# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 02:18:07 2020

@author: Bogdan Tudose
"""

#%% Source files
fPath = "C:/Users/bogda/Desktop/Python/Challenge/2020/day4/"
f = open(fPath+"d4ActualInputs.txt", "r")
# f = open(fPath+"d4DemoInputs.txt", "r")
inputsActual = f.read()
# inputs = inputsDemo
inputs=inputsActual

#%% Part 1
passports = [x for x in inputs.strip("\n").split("\n\n")]
required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
optional = ['cid']

#%% Part 1 - Find Valid Passports
validPass = []
test = passports[0]
for passp in passports:
    print("-" * 20)
    for field in required:
        if passp.find(field) == -1:
            print(passports.index(passp),"not valid", passp)
            validPass.append(0)
            break
    else:
        print(passports.index(passp),"valid",passp)
        validPass.append(1)
        continue
        
print("Total Valid:",validPass.count(1))

#%% Part 2
passportsSplit = [x.replace("\n"," ").strip().split(" ") for x in passports]
passportsClean = []
for x in passportsSplit:
    keysPass = [a.split(":")[0] for a in x]
    valsPass = [a.split(":")[1] for a in x]
    newDict = {keysPass[i]:valsPass[i] for i in range(len(keysPass))}
    passportsClean.append(newDict)

import pandas as pd
df = pd.DataFrame({"Passport Fields":passportsClean,"IsValid":validPass})

expandCols = df['Passport Fields'].apply(pd.Series)
mergeDF = pd.concat([df,expandCols], axis=1)

validPassports = mergeDF[mergeDF['IsValid']==1]
cols = ['byr','iyr','eyr']
validPassports[cols] = validPassports[cols].apply(pd.to_numeric, errors='coerce')

#%%Check 1
#birth year check - 4 digits, 1920 <= x <= 2002
#issue year check - 4 digits, 2010 <= x <= 2020
#expiration year check - 4 digits, 2020 <= x <= 2030
df1 = validPassports.copy()
df2 = df1[(df1['byr'].between(1920,2002, inclusive=True)) & 
          (df1['iyr'].between(2010,2020, inclusive=True)) &
          (df1['eyr'].between(2020,2030, inclusive=True))]

#%%Check 2
#height check; in: 59<=x<=76; cm: 150<=x<=193
df2['hgt_numeric'] = df2['hgt'].str.replace("cm","").str.replace("in","").astype(int)
df3 = df2[((df2['hgt'].str.contains("in")) & (df2['hgt_numeric'].between(59,76,inclusive=True))) |
          ((df2['hgt'].str.contains("cm")) & (df2['hgt_numeric'].between(150,193,inclusive=True)))]

#%%Check 3
#https://regex101.com/
#hair color check - # followed by 6 chars of 0-9 or a-f
#eye color check amb, blu, gry, grn, hzl, oth
#pid - 9 digit number

valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
df4 = df3[(df3['hcl'].str.contains("^#[0-9a-f]{6}",regex=True)) &
          (df3['ecl'].isin(valid_ecl)) &
          (df3['pid'].str.contains("^[0-9]{9}",regex=True))&
          (df3['pid'].str.len() == 9)]

print("Total Valid",df4.shape[0])
