# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

class Solution:
  def evalRPN(self, tokens):
      stack = []

      for token in tokens:
          if token in ('+', '-', '*', '/'):
              # Pop the two operands from the stack
              b = stack.pop()
              a = stack.pop()

              if token == '+':
                  stack.append(a + b)
              elif token == '-':
                  stack.append(a - b)
              elif token == '*':
                  stack.append(a * b)
              elif token == '/':
                  # Handle division (truncate toward zero)
                  # If a and b have different signs and the result is non-zero
                  if a * b < 0 and a % b != 0:
                      stack.append(a // b + 1)  # Adjust the result towards zero
                  else:
                      stack.append(a // b)
          else:
              # If it's a number, push it onto the stack
              stack.append(int(token))

      # The result should be the only element left in the stack
      return stack[-1]
