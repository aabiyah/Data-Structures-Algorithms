# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.Implement Queue using Stacks

class MyQueue(object):

def __init__(self):
    """
    Initialize two stacks.
    """
    self.stack1 = []  # Main stack for pushing new elements
    self.stack2 = []  # Helper stack for reversing the order

def push(self, x):
    """
    Push element x to the back of queue.
    :type x: int
    :rtype: None
    """
    self.stack1.append(x)

def pop(self):
    """
    Removes the element from in front of the queue and returns that element.
    :rtype: int
    """
    # Ensure stack2 has elements, if not, move elements from stack1 to stack2
    if not self.stack2:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
    return self.stack2.pop()

def peek(self):
    """
    Get the front element.
    :rtype: int
    """
    # Ensure stack2 has elements, if not, move elements from stack1 to stack2
    if not self.stack2:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
    return self.stack2[-1]

def empty(self):
    """
    Returns whether the queue is empty.
    :rtype: bool
    """
    return not self.stack1 and not self.stack2