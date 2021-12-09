"""
Math 560
Project 3
Fall 2021

Partner 1: Kavi Freyaldenhoven kf154
Partner 2: Francesco Mastrocinque fam21 
Date: 11/4/2021

"""
import math
from p3tests import *

################################################################################

"""
detectArbitrage
INPUTS: adjList: the adjacency list representing the currencies graph.
        adjMat: the adjacency matrix representing the exchange rates, as generated by the
        rates2mat function.
        tol: this is a value that is set at 1e-15 as default
OUTPUT: backwards_cycle: a single list of vertex ranks corresponding to the negative cost cycle
"""
def detectArbitrage(adjList, adjMat, tol=1e-15):
    # Setting adjMat = A for notation
    A = adjMat
    
    # Set initial dist and prev
    for vertex in adjList:
        vertex.dist = math.inf
        vertex.prev = None
    
    # Starting distance to 0
    adjList[0].dist = 0 
    
    # Establishing |V|
    number_of_vertices = len(adjList)
    
    # iterating |V| - 1 times
    for n in range(0,number_of_vertices-1):
        
        # look at each vertex
        for u in adjList:
            
            # check each neighbor of vertex
            # update predictions and previous vertex.
            for v in u.neigh:
                
                # only update if new value is better
                if v.dist > u.dist + A[u.rank][v.rank] + tol:
                    v.dist = u.dist + A[u.rank][v.rank]
                    v.prev = u
                    
    # iterate one more time and see if something changes
    changed_vertex_value = None
    
    # look at each vertex
    for u in adjList:
        
            # check each neighbor of vertex for a change
            for v in u.neigh:
                
                # if new value is better then we can traceback a cycle
                if v.dist > u.dist + A[u.rank][v.rank] + tol:
                    changed_vertex_value = v
                    v.dist = u.dist + A[u.rank][v.rank]
                    v.prev = u
                    
    # if NO cost cycle
    if changed_vertex_value == None:
        return []
    
    # Backwards Cycle initially starting at changed vertex
    cost_cycle_twice = False
    x = changed_vertex_value
    backwards_cycle = [x.rank]
    
    # Traceback to the cycle so we have every cycled element's rank in the list
    while cost_cycle_twice is False:
        previous_value = x.prev
        if backwards_cycle.count(previous_value.rank) < 1:
            backwards_cycle.append(previous_value.rank)
            x = previous_value
        else:
            cost_cycle_twice = True
            backwards_cycle.append(previous_value.rank)

    # Reverse list to find forward cycle         
    backwards_cycle.reverse()
    
    return backwards_cycle

################################################################################

"""
rates2mat
"""
def rates2mat(rates):
    ##### Your implementation goes here. #####
    return [[-math.log(R) for R in row] for row in rates]
    # Currently this only returns a copy of the rates matrix.
#    return [[R for R in row] for row in rates]
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testRates()