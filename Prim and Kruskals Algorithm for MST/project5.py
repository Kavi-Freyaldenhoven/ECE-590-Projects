"""
Math 560
Project 5
Fall 2021

Partner 1: Kavi Freyaldenhoven kf154
Partner 2: Francesco Mastrocinque fam21
Date:
"""

# Import math, itertools, and time.
import math
import itertools
import time
import random

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm

INPUTS: 
    adjList - the adjacency list for the map which is a list of Vertex objects
    adjMat - the adjacency matrix for the map

OUTPUTS:
        None, it just ensures that at the end of execution, every vertex has 
        been assigned the proper vertex.prev values.
"""
def prim(adjList, adjMat):
    
    # Initialize costs to infinity, prev to null, and visited to False
    for vertex in adjList:
        vertex.cost = math.inf
        vertex.prev = None
        vertex.visited = False
    
    # Pick an arbitrary start vertex and set cost to 0.
    random_number = random.randint(0,len(adjList) - 1)
    start = adjList[random_number]
    start.cost = 0
    
    # Create the priority queue using cost for sorting.
    Q = PriorityQueue()
    
    for vertex in adjList:
        Q.insert(vertex)
        
    # iterate while queue has elements 
    while Q.isEmpty() is False:
        
        # Get the next unvisited vertex and visit it.
        v = Q.deleteMin()
        v.visited = True
        
        # For each edge out of v.
        for neighbor in v.neigh:
            
            # If the edge leads out, update.
            if neighbor.visited is False:
    
                if neighbor.cost > adjMat[v.rank][neighbor.rank]:
                    neighbor.cost = adjMat[v.rank][neighbor.rank]
                    neighbor.prev = v
        
    
    return

################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.

INPUTS: 
    adjList - the adjacency list for the map which is a list of Vertex objects
    edgeList - the list of Edge objects for the map

OUTPUTS: 
    X - a list of edges that are in the MST
    
"""
def kruskal(adjList, edgeList):
    # Initialize all singleton sets for each vertex
    for vertex in adjList:
        makeset(vertex)
        
    # Initialize the empty MST
    X = []
    
    # Sort edges
    edgeList.sort()
    
    # Loop through the sorted edges
    for edge in edgeList:
        
        # If the min edge crosses a cut, add it to our MST
        u, v = edge.vertices
        
        if find(u).isEqual(find(v)) == False:
            X.append(edge)
            union(u, v)
            
    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.

INPUT: 
    v - vertex
"""
def makeset(v):
    
    v.pi = v
    v.height = 0
    
    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

INPUT: 
    v - vertex
"""
def find(v):
    
    while v != v.pi:
        v = v.pi
        
    return v

"""
union: this function will union the sets of vertices v and u.

INPUT: 
    v - vertex
    u - vertex
"""

def union(u,v):
   # Find the root of the tree for u and the tree for v
    root_u = find(u)
    root_v = find(v)
    
    # If sets are the same, return
    if root_u == root_v:
        return
    
    # Make shorter set point to taller set
    if root_u.height > root_v.height:
        root_v.pi = root_u
        
    elif root_u.height < root_v.height:
        root_u.pi = root_v
    
    else:
        # same height, break tie
        root_u.pi = root_v
        
        # Tree got taller, increment rv.height.
        root_u.height += 1
    
    return

################################################################################

"""
TSP

INPUTS: 
    adjList - the adjacency list for the map which is a list of Vertex objects
    start - starting vertex

OUTPUT:
    tour - tour array of vertex ranks.
"""
def tsp(adjList, start):
    
    #initialization of tour list and vertices
    tour = []

    for vertex in adjList:
        vertex.visited = False

    # initialize stack 
    stack = []
    
    # Push start vertex onto stack
    stack.append(start)

    # While stack is not empty
    while len(stack) > 0:
        
        # Pop current vertex
        vertex = stack.pop()
        
        # Only visit if we have not visited before
        if vertex.visited == False: 
            
            # mark it as visited and append vertex to tour list
            vertex.visited = True
            tour.append(vertex.rank)
            
            # Use mstN rather than neigh list
            for neighbor in vertex.mstN:
                
                # Push all neighbors onto the stack
                stack.append(neighbor)

    # Append the start vertex as the end of tour to complete the cycle
    tour.append(start.rank)

    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))