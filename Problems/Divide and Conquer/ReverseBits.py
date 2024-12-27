# Reverse bits of a given 32 bits unsigned integer.

    # Note:
    
    # Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
    # In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

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