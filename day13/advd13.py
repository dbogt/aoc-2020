# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 00:01:40 2020

@author: Bogdan Tudose
"""
#%% Import packages
import numpy as np

#%% Source files
fPath = "../aoc-2020-Src/"
# f = open(fPath+"d13DemoInputs.txt", "r")
f = open(fPath+"d13ActualInputs.txt", "r")
inputs = f.read()
lines = [x for x in inputs.strip("\n").split("\n")]

#%% Part 1
timeStamp = int(lines[0])
allBuses = [int(x) if x!="x" else "x" for x in lines[1].split(",")]
buses = [int(x) if x!="x" else "x" for x in lines[1].replace("x,","").split(",")]

closestTimes = []
for bus in buses:
    divisor = timeStamp // bus
    print(divisor)
    if divisor * bus < timeStamp:
        divisor +=1
    closestTimes.append(divisor * bus)
        
minTime = np.min(closestTimes)
idx = closestTimes.index(minTime)
closestBus = buses[idx]

print("Part 1 answer:", closestBus * (minTime - timeStamp) )

#%% Part 2
allBuses = [int(x) if x!="x" else "x" for x in lines[1].split(",")]
coeffs = [int(x) if x!="x" else "x" for x in lines[1].replace("x,","").split(",")]
mods = {}
for coeff in coeffs:
    idx = allBuses.index(coeff)
    mod = coeff - idx
    mods[coeff] = mod


modsList = list(mods.values())
modsCoeff = list(mods.keys())
#%%
from sympy.ntheory.modular import crt
results = crt(modsCoeff,modsList)
print(results[0])

#%% Or use functions below and the crt formula

print(crt(modsCoeff,modsList)) 
#%% Chinese Remainder Theorem
#https://www.geeksforgeeks.org/using-chinese-remainder-theorem-combine-modular-equations/    
# Python 2.x program to combine modular equations 
# using Chinese Remainder Theorem 

# function that implements Extended euclidean 
# algorithm 
def extended_euclidean(a, b): 
	if a == 0: 
		return (b, 0, 1) 
	else: 
		g, y, x = extended_euclidean(b % a, a) 
		return (g, x - (b // a) * y, y) 

# modular inverse driver function 
def modinv(a, m): 
	g, x, y = extended_euclidean(a, m) 
	return x % m 

# function implementing Chinese remainder theorem 
# list m contains all the modulii 
# list x contains the remainders of the equations 
def crt(m, x): 

	# We run this loop while the list of 
	# remainders has length greater than 1 
	while True: 
		
		# temp1 will contain the new value 
		# of A. which is calculated according 
		# to the equation m1' * m1 * x0 + m0' 
		# * m0 * x1 
		temp1 = modinv(m[1],m[0]) * x[0] * m[1] + modinv(m[0],m[1]) * x[1] * m[0] 

		# temp2 contains the value of the modulus 
		# in the new equation, which will be the 
		# product of the modulii of the two 
		# equations that we are combining 
		temp2 = m[0] * m[1] 

		# we then remove the first two elements 
		# from the list of remainders, and replace 
		# it with the remainder value, which will 
		# be temp1 % temp2 
		x.remove(x[0]) 
		x.remove(x[0]) 
		x = [temp1 % temp2] + x 

		# we then remove the first two values from 
		# the list of modulii as we no longer require 
		# them and simply replace them with the new 
		# modulii that we calculated 
		m.remove(m[0]) 
		m.remove(m[0]) 
		m = [temp2] + m 

		# once the list has only one element left, 
		# we can break as it will only contain 
		# the value of our final remainder 
		if len(x) == 1: 
			break

	# returns the remainder of the final equation 
	return x[0] 


    
