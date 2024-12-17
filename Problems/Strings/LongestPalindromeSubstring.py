class Solution(object):
  def longestPalindrome(self, s):
      n = len(s)
      if n == 0:
          return ""

      # Initialize the DP table
      dp = [[False] * n for _ in range(n)]

      # Variables to track the start and length of the longest palindrome
      start = 0
      max_length = 1

      # Every single character is a palindrome
      for i in range(n):
          dp[i][i] = True

      # Check for two-character palindromes
      for i in range(n - 1):
          if s[i] == s[i + 1]:
              dp[i][i + 1] = True
              start = i
              max_length = 2

      # Check for palindromes of length > 2
      for length in range(3, n + 1):  # length of substring
          for i in range(n - length + 1):  # starting index
              j = i + length - 1  # ending index

              # Check if s[i:j+1] is a palindrome
              if s[i] == s[j] and dp[i + 1][j - 1]:
                  dp[i][j] = True
                  start = i
                  max_length = length

      # Extract the longest palindromic substring
      return s[start:start + max_length]
Longest Palindromic Substring