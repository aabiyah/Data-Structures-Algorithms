# Design your implementation of the circular double-ended queue (deque).

# Implement the MyCircularDeque class:

# MyCircularDeque(int k) Initializes the deque with a maximum size of k.
# boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
# boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
# int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
# int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
# boolean isEmpty() Returns true if the deque is empty, or false otherwise.
# boolean isFull() Returns true if the deque is full, or false otherwise.
Design Circular Deque
class MyCircularDeque:

def __init__(self, k):
    """
    :type k: int
    """
    self.queue = [0] * k  # Fixed-size array for the deque
    self.size = k         # Maximum size of the deque
    self.front = 0        # Pointer to the front
    self.rear = -1        # Pointer to the rear
    self.count = 0        # Current number of elements

def insertFront(self, value):
    """
    :type value: int
    :rtype: bool
    """
    if self.isFull():
        return False
    self.front = (self.front - 1 + self.size) % self.size  # Move front pointer backward in a circular manner
    self.queue[self.front] = value  # Insert value at front
    self.count += 1
    return True

def insertLast(self, value):
    """
    :type value: int
    :rtype: bool
    """
    if self.isFull():
        return False
    self.rear = (self.rear + 1) % self.size  # Move rear pointer forward in a circular manner
    self.queue[self.rear] = value  # Insert value at rear
    self.count += 1
    return True

def deleteFront(self):
    """
    :rtype: bool
    """
    if self.isEmpty():
        return False
    self.front = (self.front + 1) % self.size  # Move front pointer forward in a circular manner
    self.count -= 1
    return True

def deleteLast(self):
    """
    :rtype: bool
    """
    if self.isEmpty():
        return False
    self.rear = (self.rear - 1 + self.size) % self.size  # Move rear pointer backward in a circular manner
    self.count -= 1
    return True

def getFront(self):
    """
    :rtype: int
    """
    if self.isEmpty():
        return -1
    return self.queue[self.front]

def getRear(self):
    """
    :rtype: int
    """
    if self.isEmpty():
        return -1
    return self.queue[self.rear]

def isEmpty(self):
    """
    :rtype: bool
    """
    return self.count == 0

def isFull(self):
    """
    :rtype: bool
    """
    return self.count == self.size
