class Solution:
  def reverseBits(self, n):
      """
      :type n: int
      :rtype: int
      """
      result = 0
      for i in range(32):  # Process all 32 bits
          # Extract the LSB of n
          bit = n & 1
          # Shift the bit to its reversed position and add it to the result
          result = (result << 1) | bit
          # Right shift n to process the next bit
          n >>= 1
      return result