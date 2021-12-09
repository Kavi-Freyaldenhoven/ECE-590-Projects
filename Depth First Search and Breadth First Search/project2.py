"""
Math 560
Project 2
Fall 2021

project2.py

Kavi Freyaldenhoven kf154
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')
    
    if alg == 'DFS':
        
        # initiazlizing start vertex and intiial vertex values
        starting_vertex = maze.start
        
        for vertex in maze.adjList:
            vertex.visited = False
            vertex.prev = None
        
        # creating stack and pushing start onto stack
        stack = Stack()
        
        starting_vertex.visited = True
        stack.push(starting_vertex)
        
        # iterate while there are still vertices to visit
        while stack.numElems > 0:
            current = stack.pop()
            
            # visit neighbor for each vertex, noting where you came from
            for i in range(len(current.neigh)):
                if current.neigh[i].visited is False:
                    current.neigh[i].visited = True
                    stack.push(current.neigh[i])
                    current.neigh[i].prev = current
                    
        # trace back to beginning
        reversed_escape = []
        trace_back = maze.exit
        
        while trace_back != None:
            reversed_escape.append(trace_back.rank)
            trace_back = trace_back.prev
        
        reversed_escape.reverse()
        
    if alg == 'BFS':
        
        # initiazlizing start vertex and intiial vertex values
        starting_vertex = maze.start
        
        for vertex in maze.adjList:
            vertex.visited = False
            vertex.prev = None
        # creating queue and pushing start onto queue   
        queue = Queue()
        
        starting_vertex.visited = True
        queue.push(starting_vertex)
        
        # iterate while there are still vertices to visit
        while queue.numElems > 0:
            current = queue.pop()
            
            # visit neighbor for each vertex, noting where you came from
            for i in range(len(current.neigh)):
                if current.neigh[i].visited is False:
                    current.neigh[i].visited = True
                    queue.push(current.neigh[i])
                    current.neigh[i].prev = current
        
         # trace back to beginning
        reversed_escape = []
        trace_back = maze.exit
        
        while trace_back != None:
            reversed_escape.append(trace_back.rank)
            trace_back = trace_back.prev
        
        reversed_escape.reverse()
        
        
    return reversed_escape

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
