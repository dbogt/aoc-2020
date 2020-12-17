# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 00:47:16 2020

@author: Bogdan Tudose
"""
#%% Packages
import itertools

#%% Source files
fPath = "../aoc-2020-Src/"
# f = open(fPath+"d17DemoInputs.txt", "r")
f = open(fPath+"d17ActualInputs.txt", "r")
inputs = f.read()
lines = [x for x in inputs.strip("\n").split("\n")]

#%% Part 1
mapCubes = {}
z = 0
#create initial map
for y, line in enumerate(lines):
    for x, cube in enumerate(line):
        isActive = cube == "#"
        mapCubes[(x, y, z)] = isActive
        
neighbours = [x for x in itertools.product([-1,0,1], repeat=3)]
neighbours.remove((0,0,0))
#%% Functions

def getNeighbours(cube):
    x, y, z = cube
    adjCubes = []
    for dx, dy, dz in neighbours:
        adjCubes.append((x+dx, y+dy, z+dz))
    return adjCubes
 
def countActiveNeighbours(cube):
    checkNeighbours = getNeighbours(cube)
    numActive = 0
    for cube in checkNeighbours:
        if mapCubes.get(cube, False):
            numActive +=1
    return numActive
    
    
#%% Part 1
for cycle in range(6):
     activeNeighbours = {}
     nextMap = mapCubes.copy()
     allNeighbours = []
     for cube in mapCubes.keys():
         currCubeNeighbours = getNeighbours(cube)
         allNeighbours.extend(currCubeNeighbours)
         allNeighbours = list(set(allNeighbours))
     for neighb in allNeighbours:
         activeNeighbours[neighb] = countActiveNeighbours(neighb)
     for cube, numActive in activeNeighbours.items():
         isActive = mapCubes.get(cube, False)
         #if currently inactive check if exactly 3 neighbs are active
         if not isActive and numActive == 3:
             nextMap[cube] = True
         #if currently active, turn inactive if exactly 2 or 3 neighbs are NOT active
         elif isActive and not (numActive == 2 or numActive == 3):
             nextMap[cube] = False
     mapCubes = nextMap       

print("Part 1 - total active cubes:",list(mapCubes.values()).count(True))