# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

class Solution:
  def isHappy(self, n: int) -> bool:
      def sum_of_squares(num):
          # Calculate the sum of squares of digits of the number
          return sum(int(digit) ** 2 for digit in str(num))

      seen = set()  # To track numbers we've encountered

      while n != 1:
          if n in seen:
              # If n is already in seen, we are in a cycle, return False
              return False
          seen.add(n)
          n = sum_of_squares(n)  # Replace n with the sum of squares of its digits

      return True  # If we reach 1, it's a happy number
