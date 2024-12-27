# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

# The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

class Solution:
  def diffWaysToCompute(self, expression):
      # Dictionary to store the computed results for subexpressions
      memo = {}

      # Helper function to compute the results
      def compute(expr):
          # If this subexpression has been computed before, return the stored result
          if expr in memo:
              return memo[expr]

          # If the expression is just a number, return its integer value
          if expr.isdigit():
              return [int(expr)]

          # List to store the results for the current expression
          results = []

          # Loop through the expression to find operators
          for i in range(len(expr)):
              if expr[i] in '+-*':
                  # Split the expression into left and right parts around the operator
                  left = expr[:i]
                  right = expr[i+1:]

                  # Recursively compute the results for both left and right parts
                  left_results = compute(left)
                  right_results = compute(right)

                  # Combine the results from the left and right sides using the operator
                  for l in left_results:
                      for r in right_results:
                          if expr[i] == '+':
                              results.append(l + r)
                          elif expr[i] == '-':
                              results.append(l - r)
                          elif expr[i] == '*':
                              results.append(l * r)

          # Memoize the result for this expression
          memo[expr] = results
          return results

      # Call the helper function on the full expression
      return compute(expression)