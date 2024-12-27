# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

class Solution(object):
  def myPow(self, x, n):
      """
      :type x: float
      :type n: int
      :rtype: float
      """
       # Edge case: if n is 0, x^0 is always 1 (except when x is 0, but 0^0 is undefined)
      if n == 0:
          return 1.0

      # If n is negative, we compute the power for positive n and take the reciprocal
      if n < 0:
          x = 1 / x
          n = -n

      result = 1
      while n > 0:
          # If n is odd, multiply result by current x
          if n % 2 == 1:
              result *= x
          # Square x and halve n
          x *= x
          n //= 2

      return result