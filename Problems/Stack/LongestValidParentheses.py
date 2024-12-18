# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring. 

class Solution(object):
  def longestValidParentheses(self, s):
      """
      :type s: str
      :rtype: int
      """
      stack = [-1]  # Initialize stack with base index
      max_len = 0  # To store the maximum length of valid parentheses substring

      # Iterate through the string
      for i, char in enumerate(s):
          if char == '(':  # Push index of '(' onto stack
              stack.append(i)
          else:
              # Pop the last open parenthesis index
              stack.pop()

              # If the stack is not empty, calculate the valid substring length
              if stack:
                  max_len = max(max_len, i - stack[-1])
              else:
                  # If the stack is empty, push the current index as a new base
                  stack.append(i)

      return max_len
