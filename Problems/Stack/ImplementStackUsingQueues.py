# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Push the new element to the secondary queue
        self.q2.append(x)

        # Transfer all elements from q1 to q2 to maintain stack order
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Swap the names of q1 and q2 so q1 always acts as the primary queue
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """
        :rtype: int
        """
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q1.popleft()  # The first element of q1 is the top of the stack


    def top(self):
        """
        :rtype: int
        """
        """
        Get the top element.
        :rtype: int
        """
        return self.q1[0]  # Peek the front of q1, which is the top of the stack

    def empty(self):
        """
        :rtype: bool
        """
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.q1  # Return True if q1 is empty, False otherwise


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()