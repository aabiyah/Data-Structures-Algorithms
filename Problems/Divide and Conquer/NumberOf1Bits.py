# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

class Solution:
  def hammingWeight(self, n):
      """
      :type n: int
      :rtype: int
      """
      count = 0
      while n:
          count += n & 1  # Check if the LSB is 1
          n >>= 1         # Right shift n by 1 to process the next bit
      return count