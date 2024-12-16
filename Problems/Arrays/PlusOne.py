# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's. Increment the large integer by one and return the resulting array of digits.

class Solution(object):
  def plusOne(self, digits):
      # Start from the last digit and add 1
      for i in range(len(digits) - 1, -1, -1):
          if digits[i] < 9:
              digits[i] += 1
              return digits
          digits[i] = 0  # Carry over the 1

      # If all digits were 9, add a leading 1
      return [1] + digits
