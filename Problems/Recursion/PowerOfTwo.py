# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution:
  def isPowerOfTwo(self, n):
      # Check if n is positive and if n & (n - 1) is 0
      return n > 0 and (n & (n - 1)) == 0