"""
Math 560
Project 4
Fall 2021

Partner 1: Kavi Freyaldenhoven kf154
Partner 2: Francesco Mastrocinque fam21 
Date: 11/19/21
"""

# Import p4tests.
from p4tests import *

################################################################################

"""
ED: the edit distance function which uses dynamic programming to perform the 
edit distance algorithm. It finds thenumber of edits required to convert src
to dest and a list of edits to perform

Inputs: 
    src - a string which we will convert
    dest - a string which is what we want to convert src into

Outputs: 
    number_of_moves_needed- the toal number of edits to perform
    traceback_array - a list of the edits to perform
    
"""
def ED(src, dest, prob='ED'):
    # Check the problem to ensure it is a valid choice.
    if (prob != 'ED') and (prob != 'ASM'):
        raise Exception('Invalid problem choice!')
    
    S1 = src
    S2 = dest
    
    # creating array
    dynamic_table = [[None for j in range(len(S2) + 1)] for k in range(len(S1) + 1)]
    
    # filling in base cases depending on function call
    
    if prob == 'ED':
        for i in range(len(dynamic_table[0])):
            dynamic_table[0][i] = i
    else:
        for i in range(len(dynamic_table[0])):
            dynamic_table[0][i] = 0
        
    for i in range(len(dynamic_table)):
        dynamic_table[i][0] = i 
    
    # filling in table entries using base case
    
    for i in range(1,len(dynamic_table)):
        for j in range(1,len(dynamic_table[0])):
            
            if S1[i-1] == S2[j-1]:
                dynamic_table[i][j] = dynamic_table[i-1][j-1]
                
            else:
                a = dynamic_table[i][j-1]
                b = dynamic_table[i-1][j]
                c = dynamic_table[i-1][j-1]
                
                dynamic_table[i][j] = 1 + min(a,b,c)
    
    # total changes is the bottom right entry of the matrix
    number_of_moves_needed = dynamic_table[len(dynamic_table)-1][len(dynamic_table[0])-1]
    
    # now for the traceback
    
    # initialize i and j and empty array
    i = len(dynamic_table)-1
    j = len(dynamic_table[0])-1
    
    traceback_array = []
    
    # loop through to get us back to a base case and track which changes
    while i > 0 and j > 0:
        
        if S1[i-1] == S2[j-1]:
            traceback_array.append(('match', S1[i-1], i-1))
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
                traceback_array.append(('delete', S1[i-1], i-1))
                i -= 1
                
            else:
                traceback_array.append(('sub', S2[j-1], i-1))
                i -= 1
                j -= 1
                
    # Now we're at a base case
    
    # if i = 0 we just insert until j = 0 
    while i == 0 and j > 0:
        traceback_array.append(('insert', S2[j-1], i))
        j -= 1
    
    # if j = 0 we just delete until i = 0 
    while j == 0 and i > 0:
        traceback_array.append(('delete', S1[i-1], i-1))
        i -= 1
           
        
    return number_of_moves_needed, traceback_array

################################################################################

"""
Main function.
"""
if __name__ == "__main__":
    edTests(False)
    print()
    compareGenomes(True, 30, 300, 'ED')
    print()
    compareRandStrings(True, 30, 300, 'ED')
    print()
    compareGenomes(True, 30, 300, 'ASM')
    print()
    compareRandStrings(True, 30, 300, 'ASM')