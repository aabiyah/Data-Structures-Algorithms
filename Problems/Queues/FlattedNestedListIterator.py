# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

# Implement the NestedIterator class:

# NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
# Your code will be tested with the following pseudocode:

# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
#     append iterator.next() to the end of res
# return res
# If res matches the expected flattened list, then your code will be judged as correct.

class NestedIterator:
    def __init__(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        """
        # Initialize the stack with the nested list in reverse order
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        # hasNext ensures the next element is an integer, so we can safely pop
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        # Process the stack until we find an integer at the top or the stack is empty
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True  # Top element is an integer
            else:
                # Top element is a list, expand it by replacing it with its contents
                self.stack.pop()
                self.stack.extend(top.getList()[::-1])
        return False
