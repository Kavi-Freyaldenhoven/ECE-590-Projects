"""
Math 560
Project 2
Fall 2021

p2queue.py

Partner 1: Kavi Freyaldenhoven kf154
Partner 2: Francesco Mastrocinque fam21
Date:
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 3.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
        s += ('Front: %d' % self.front) + '\n'
        s += ('Rear: %d' % self.rear) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the queue is full.
    
    Input: self - This is a method so it will simply look at the queue object which 
    the function is called to evaluate
    
    Output: Boolean statement which tells us whether or not the queue is full
    """
    def isFull(self):
        
        # initializing boolean and i counter
        
        full = True
        i = 0
        
        
        # while loop to look at all array locations and check if they are filled
        while full is True and i < len(self.queue):
            if self.queue[i] == None:
                
                # Once we find a single location not filled, the loop terminates
                full = False
            i += 1
            
        return full

    """
    isEmpty function to check if the queue is empty.
    
    Input: self - This is a method so it will simply look at the queue object which 
    the function is called to evaluate
    
    Output: Boolean statement which tells us whether or not the queue is full
    """
    def isEmpty(self):
        
        # initializing boolean and i counter
        empty = True
        i = 0
        
        # while loop to look at all array locations and check if they are empty
        while empty is True and i < len(self.queue):
            if self.queue[i] != None:
                
                # Once we find a single element the loop terminates
                empty = False
            i += 1
            
        return empty

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    
    Input: self - This is a method so it will simply look at the queue object 
    which the function is called on, and double its array length
    
    Output:  self - the same queue, but doubled in length
    """
    def resize(self):
        array_size = len(self.queue)
        
        # unwrapping the queue if it has been wrapped
        if self.rear <= self.front:
            self.queue = self.queue[self.front:] + self.queue[0:self.rear]
        
        # resetting the indices
        self.front = 0
        self.rear = array_size
        
        # doubling length and filling the initial spots
        doubled_array = [None for i in range(2 * array_size)]
        doubled_array[:len(self.queue)] = self.queue[:]
        
        self.queue = doubled_array
        
        return

    """
    push function to push a value into the rear of the queue.
    
    Inputs: self - This is a method so it will apply the function to the queue
    
            val = the value pushed into the back of the queue
    
    Output: self - the same queue but with val appended to the back
    """
    def push(self, val):
        
        # resize if full
        if self.isFull() == True:
            self.resize()
            
        A = self.queue
        
        # pushing val at rear
        A[self.rear] = val
        
        # increasing indices 
        self.rear += 1
        self.numElems += 1
        
        # wrapping around rear index if index out of range
        if self.rear + 1 > len(A):
            self.rear = self.rear % len(A)
        
        return

    """
    pop function to pop the value from the front of the queue.
    
    Inputs: self - This is a method so it will apply the function to the queue
    
    
    Output: popped_element - the element at the front of queue
    """
    
    def pop(self):
        A = self.queue
        
        # popping element 
        popped_element = A[self.front]
        A[self.front] = None
        
        # increasing index
        self.front += 1
        
        # wrapping around front index if out of range
        if self.front + 1 > len(A):
            self.front = self.front % len(A)
        
        # decreasing index
        self.numElems -= 1
        
        return popped_element