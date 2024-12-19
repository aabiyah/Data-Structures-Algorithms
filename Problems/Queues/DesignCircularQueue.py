# Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

# Implement the MyCircularQueue class:

  # MyCircularQueue(k) Initializes the object with the size of the queue to be k.
  # int Front() Gets the front item from the queue. If the queue is empty, return -1.
  # int Rear() Gets the last item from the queue. If the queue is empty, return -1.
  # boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
  # boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
  # boolean isEmpty() Checks whether the circular queue is empty or not.
  # boolean isFull() Checks whether the circular queue is full or not.
# You must solve the problem without using the built-in queue data structure in your programming language. 

class MyCircularQueue:

def __init__(self, k):
    """
    :type k: int
    """
    self.queue = [0] * k  # Array to store queue elements
    self.size = k  # Maximum size of the queue
    self.front = 0  # Pointer to the front of the queue
    self.rear = -1  # Pointer to the rear of the queue
    self.count = 0  # Current number of elements in the queue

def enQueue(self, value):
    """
    :type value: int
    :rtype: bool
    """
    if self.isFull():
        return False
    self.rear = (self.rear + 1) % self.size  # Move rear pointer in circular manner
    self.queue[self.rear] = value  # Insert value
    self.count += 1  # Increment count
    return True

def deQueue(self):
    """
    :rtype: bool
    """
    if self.isEmpty():
        return False
    self.front = (self.front + 1) % self.size  # Move front pointer in circular manner
    self.count -= 1  # Decrement count
    return True

def Front(self):
    """
    :rtype: int
    """
    if self.isEmpty():
        return -1
    return self.queue[self.front]

def Rear(self):
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
