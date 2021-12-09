"""
Math 560
Project 1
Fall 2021

Kavi Freyaldenhoven kf154

    

"""

"""
SelectionSort: This algorithm separates the array into a sorted component 
and an unsorted component. Then it iteratively searches the unsorted component 
for the minimum element, then places it at the end of the sorted component

Inputs: 
listToSort - An array of numbers which we want to sort

Outputs:
listToSort - The sorted input array
"""

def SelectionSort(listToSort):
    
    # k index separating the sorted elements from the unsorted ones
    for k in range(len(listToSort)):
        
        # Finding the index of the minimum value of the unsorted elements
        for i in range(k,len(listToSort)):
            min_index = k
            if listToSort[i] < listToSort[k]:
                    min_index = i
                    
                    # place minimum value at the end of the sorted component
                    tempval = listToSort[k]
                    listToSort[k] = listToSort[min_index]
                    listToSort[min_index] = tempval
        
    return listToSort

"""
InsertionSort: This algorithm separates the array into a sorted component 
and an unsorted component. Then it iteratively inserts the first unsorted 
element into the correct place among the sorted elements

Inputs: 
listToSort - An array of numbers which we want to sort

Outputs:
listToSort - The sorted input array
"""
def InsertionSort(listToSort):
    
    # k index separating the sorted elements from the unsorted ones
    for k in range(len(listToSort)-1):
        
        # searching backwards through the sorted component to place unsorted element
        for i in range(k,-1,-1):
            
            # bubbling element into the correct location
            if listToSort[i+1] < listToSort[i]:
                tempval = listToSort[i+1]
                listToSort[i+1] = listToSort[i]
                listToSort[i] = tempval
            else:
                break
            
    return listToSort

"""
BubbleSort: This algorithm iterates through the array, comparing every two
adjacent elements. If they are out of over, they are swapped. This process
repeats until there is a complete iteration where no swaps are made.

Inputs: 
listToSort - An array of numbers which we want to sort

Outputs:
listToSort - The sorted input array
"""
def BubbleSort(listToSort):
    
    # initializing swaps_made variable
    swaps_made = True
    
    # Iterate until no swap occurs
    while swaps_made == True:
        swaps_made = False
        
        # Comparing every two adjacent elements
        for k in range(len(listToSort)-1):
            
            # Swapping elements if they are out of order
            if listToSort[k+1] < listToSort[k]:
                swaps_made = True
                tempval = listToSort[k+1]
                listToSort[k+1] = listToSort[k]
                listToSort[k] = tempval
                
    return listToSort


"""
MergeSort: A divide and conquer algorithm which splits the array in half,
recursively sorts each half, and then merges the two already sorted halves.

Inputs: 
listToSort - An array of numbers which we want to sort

Outputs:
listToSort - The sorted input array

"""
def MergeSort(listToSort):
    
        # base cases
    if len(listToSort) == 1:
        return listToSort
    
    if len(listToSort) == 2:
        if listToSort[1] < listToSort[0]:
            tempval = listToSort[0]
            listToSort[0] = listToSort[1]
            listToSort[1] = tempval
        return listToSort
    
    #splitting the list
    mid_point = int(len(listToSort)/2)
    
    L1 = [listToSort[i] for i in range (mid_point)]
    L2 = [listToSort[i] for i in range(mid_point,len(listToSort))]
    
    # calling mergesort on both lists
    L1 = MergeSort(L1)
    L2 = MergeSort(L2)
    
    # MERGING TWO SORTED LISTS
    
    # defining list lengths
    L1_length = len(L1)
    L2_length = len(L2)
    
    final_list_length = L1_length + L2_length
    
    # preallocating L
    L = [0 for i in range(final_list_length)]
    
    #initializing i and j
    i = 0
    j = 0
    
    # going through L1 and L2 until one indice is out of range
    while i < L1_length and j < L2_length:
        if L1[i] < L2[j]:
            L[i+j] = L1[i]
            i += 1
        else:
            L[i+j] = L2[j]
            j += 1
    
    # depending on which indice went out of range we fill with the other      
    while i < L1_length:
        L[i+j] = L1[i]
        i += 1
        
    while j < L2_length:
        L[i+j] = L2[j]
        j += 1
    
    # copying sorted values into the input list
    listToSort[0:len(listToSort)] = L[0:len(L)]
    
    return listToSort

"""
QuickSort: A divide and conquer algorithm which partitions an array based off
the pivot, putting everything smaller than the pivot the left and everything
larger to the right. Then it recurses on each partition

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.

Inputs:
listToSort - An array of numbers which we want to sort
i, j - Helper indices to allow us to recursively call the function on the 
partitions created

Outputs:
listToSort - The sorted input array

"""
def QuickSort(listToSort, i=0, j=None):
    
    # Set default value for j if None
    if j == None:
        j = len(listToSort)
        
    # base case    
    if i + 1 >= j:
        return listToSort
    
    # initializing a, b, and pivot value
    a = i
    b = j - 1
    pivot_value = listToSort[a]
    
    # iterating until a and b meet
    while a < b:
        # moving a forward when it's less than pivot
        if listToSort[a] < pivot_value:
            a += 1
        # moving b forward if it's greater than pivot
        elif listToSort[b] > pivot_value:
            b -= 1
        # moving a forward if both a and b equal the pivot     
        elif listToSort[a] == pivot_value and listToSort[b] == pivot_value:
            a += 1
        
        # when a and b are stuck, swap the two elements
        else:
            tempval = listToSort[a]
            listToSort[a] = listToSort[b]
            listToSort[b] = tempval
            
    # making pivot where and and b meet       
    pivot_index = a
    
    QuickSort(listToSort, i, pivot_index)
    QuickSort(listToSort,pivot_index + 1, j)
    
    return listToSort
        
"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)
