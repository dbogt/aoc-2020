# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 01:15:01 2020

@author: Bogdan Tudose
"""
#%% Source files
fPath = "day5/"
# f = open(fPath+"d5DemoInputs.txt", "r")
f = open(fPath+"d5ActualInputs.txt", "r")

inputs = f.read()
#%% Import packages
import pandas as pd

#%% Function to find seat
def findSeat(planeRows, planeCols, code):
    #Finding Row
    start = 0
    end = planeRows -1
    for x in code[0:7]:
        middle = (end - start + 1) / 2
        if x == "F":
            newStart = start
            newEnd = newStart + middle - 1
        elif x =="B":
            newStart = start + middle
            newEnd = end
        start = newStart
        end = newEnd
        if start == end:
            finalRow = int(start)
    #Finding Column
    start = 0
    end = planeCols -1
    
    for y in code[7:]:
        middle = (end - start + 1) / 2
        if y == "L":
            newStart = start
            newEnd = newStart + middle - 1
        elif y =="R":
            newStart = start + middle
            newEnd = end
        start = newStart
        end = newEnd
        if start == end:
            finalCol = int(start)
    
    seatID = finalRow * 8 + finalCol
    seatData = {"code":code,"row":finalRow,"column":finalCol,"seatID":seatID}
    return seatData
#%% Part 1
codes = [x for x in inputs.strip("\n").split("\n")]
seats = []
rows = 128
cols = 8

for code in codes:
    seats.append(findSeat(rows, cols, code)) 

df = pd.DataFrame(seats)
maxSeatID = df['seatID'].max()
minSeatID = df['seatID'].min()
#%% Part 2
allSeatIDs = [x for x in range(minSeatID, maxSeatID +1)]
currentSeats = list(df['seatID'])

for sID in allSeatIDs:
    if sID in currentSeats:
        print(sID,"found")
    else:
        print("found seat!",sID)
        break
#%% Meta Data
"""
https://adventofcode.com/2020/day/5
First 7 chars - F, B, front or back
128 rows on the plane, #0 to 127
- binary search, e.g. FBF --> first half (0 to 63), second half (32-63), etc.

Last 3 chars - L, R, left or right
8 columns on the plane, #0 to 7
- binary searc, e.g. LRL --> lower half (0 to 3), second half (4 to 8)

"""
