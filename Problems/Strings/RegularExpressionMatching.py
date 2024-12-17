# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character.Regular Expression Matching
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

class Solution(object):
  def isMatch(self, s, p):
       # Initialize DP table with False values
      dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

      # Empty pattern matches empty string
      dp[0][0] = True

      # Handle the case when the pattern is something like a*b*c* (matching empty string)
      for j in range(1, len(p) + 1):
          if p[j - 1] == '*':
              dp[0][j] = dp[0][j - 2]

      # Fill the DP table
      for i in range(1, len(s) + 1):
          for j in range(1, len(p) + 1):
              if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                  dp[i][j] = dp[i - 1][j - 1]
              elif p[j - 1] == '*':
                  dp[i][j] = dp[i][j - 2]  # '*' matches zero occurrences of the preceding element
                  if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                      dp[i][j] = dp[i][j] or dp[i - 1][j]

      return dp[len(s)][len(p)]
