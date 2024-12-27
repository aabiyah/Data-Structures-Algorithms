# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
  def generateParenthesis(self, n):
      result = []

      def backtrack(s, open_count, close_count):
          # If the current string is valid (length == 2*n), add it to the result
          if len(s) == 2 * n:
              result.append(s)
              return

          # Add an opening parenthesis if we haven't used all of them
          if open_count < n:
              backtrack(s + '(', open_count + 1, close_count)

          # Add a closing parenthesis if we haven't added more closing than opening
          if close_count < open_count:
              backtrack(s + ')', open_count, close_count + 1)

      # Start backtracking with an empty string and 0 opening and closing parentheses
      backtrack("", 0, 0)

      return result