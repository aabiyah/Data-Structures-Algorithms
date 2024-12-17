class Solution(object):
  def isValid(self, s):
      # Dictionary to map closing brackets to opening brackets
      bracket_map = {')': '(', '}': '{', ']': '['}
      stack = []  # Stack to keep track of opening brackets

      for char in s:
          # If it's a closing bracket
          if char in bracket_map:
              # Pop the last opening bracket from the stack (or use a dummy value if the stack is empty)
              top_element = stack.pop() if stack else '#'

              # Check if the popped element matches the expected opening bracket
              if bracket_map[char] != top_element:
                  return False
          else:
              # If it's an opening bracket, push it onto the stack
              stack.append(char)

      # If the stack is empty, all brackets are matched
      return not stack
