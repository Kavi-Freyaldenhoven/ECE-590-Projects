"""
Math 560
Project 2
Fall 2021

p2stack.py

Partner 1: Kavi Freyaldenhoven kf154
Partner 2: Francesco Mastrocinque fam21
Date:
"""

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 3.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=3):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.stack)) + ' ]\n'
        s += ('Top: %d' % self.top) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the stack is full.
    
    Input: self - This is a method so it will simply look at the stack object which 
    the function is called to evaluate
    
    Output: Boolean statement which tells us whether or not the stack is full
    """
    def isFull(self):
        
        # initializing boolean and i counter

        full = True
        i = 0
        
        # while loop to look at all array locations and check if they are filled
        while full is True and i < len(self.stack):
            if self.stack[i] == None:
                # Once we find a single location not filled, the loop terminates
                full = False
            i += 1
            
        return full

    """
    isEmpty function to check if the stack is empty.
    
     Input: self - This is a method so it will simply look at the stack object which 
    the function is called to evaluate
    
    Output: Boolean statement which tells us whether or not the stack is full
    """
    def isEmpty(self):
        
        # initializing boolean and i counter
        empty = True
        i = 0
        
        # while loop to look at all array locations and check if they are empty
        while empty is True and i < len(self.stack):
            if self.stack[i] != None:
                # Once we find a single element the loop terminates
                empty = False
            i += 1
            
        return empty

    """
    resize function to resize the stack by doubling its size.
    
    Input: self - This is a method so it will simply look at the stack object 
    which the function is called on, and double its array length
    
    Output:  self - the same stack, but doubled in length
    """
    def resize(self):
        
        # creating array size of double length 
        array_size = len(self.stack)
        doubled_array = [None for i in range(2 * array_size)]
        
        # filling first half with original array
        doubled_array[:len(self.stack)] = self.stack[:]
        
        self.stack = doubled_array
        
        return self.stack

    """
    push function to push a value onto the stack.
    
    Inputs: self - This is a method so it will apply the function to the stack
    
            val = the value pushed into the back of the stack
    
    Output: self - the same stack but with val appended to the back
    """
    def push(self, val):
        
        # resize if full
        if self.isFull() == True:
            self.resize()
        
        # pushing val to top of list or shifting list and then inserting val
        if self.stack[0] == None:
            self.stack[0] = val 
            
        else:
            self.stack = [self.stack[-1]] + self.stack[:-1]
    
            self.stack[0] = val
        
        # increasing index
        self.numElems += 1
        
        # if there is an element at the top of the stack, it is the first index
        if self.stack[0] != None:
            self.top = 0
        
        return

    """
    pop function to pop the value off the top of the stack.
    
    
    Inputs: self - This is a method so it will apply the function to the stack
    
    
    Output: popped_element - the element at the front of stack
    """
    def pop(self):
        
        # popped value is top of stack
        popped_val = self.stack[0]
        
        # shifting stack to reflect popped value
        self.stack[0] = None
        self.stack = self.stack[1:] + [self.stack[0]]
        
        # if nonempty stack, top is first index
        if self.stack[0] != None:
            self.top = 0
        else:
            self.top = -1
        
        # adjusting indices
        self.numElems -= 1
        
        return popped_val