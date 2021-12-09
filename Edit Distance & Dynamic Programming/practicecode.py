#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 00:47:27 2021

@author: kavif
"""

S1 = 'libate'
S2 = 'flub'

# creating array
dynamic_table = [[None for j in range(len(S2) + 1)] for k in range(len(S1) + 1)]

## filling in base case

for i in range(len(dynamic_table[0])):
        dynamic_table[0][i] = i
#else:
#    for i in range(len(dynamic_table[0])):
#        dynamic_table[0][i] = 0
    
for i in range(len(dynamic_table)):
    dynamic_table[i][0] = i 


for i in range(1,len(dynamic_table)):
    for j in range(1,len(dynamic_table[0])):
        
        if S1[i-1] == S2[j-1]:
            dynamic_table[i][j] = dynamic_table[i-1][j-1]
            
        else:
            a = dynamic_table[i][j-1]
            b = dynamic_table[i-1][j]
            c = dynamic_table[i-1][j-1]
            
            dynamic_table[i][j] = 1 + min(a,b,c)

number_of_moves_needed = dynamic_table[len(dynamic_table)-1][len(dynamic_table[0])-1]

# now for the traceback
i = len(dynamic_table)-1
j = len(dynamic_table[0])-1

traceback_array = []


while i > 0 and j > 0:
    
    if S1[i-1] == S2[j-1]:
        traceback_array.append(('match', S1[i-1], j))
        i -= 1
        j -= 1
    else:
        a = dynamic_table[i][j-1]
        b = dynamic_table[i-1][j]
        c = dynamic_table[i-1][j-1] 
         
        if min(a,b,c) == a:
            traceback_array.append(('insert', S2[j-1], i))
            j -= 1
        elif min(a,b,c) == b:
            traceback_array.append(('delete', S1[i-1], i))
            i -= 1
            
        else:
            traceback_array.append(('sub', S2[j-1], j))
            i -= 1
            j -= 1
            
# Now we're at a base case
# if i = 0 we just insert until j = 0 
while i == 0 and j > 0:
    traceback_array.append(('insert', S2[j-1], i))
    j -= 1

# if j = 0 we just delete until i = 0 
while j == 0 and i > 0:
    traceback_array.append(('delete', S1[i-1], j))
    i -= 1  
       
#if __name__ == "__main__":
    