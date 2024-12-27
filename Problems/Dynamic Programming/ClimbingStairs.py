# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution(object):
  def climbStairs(self, n):
      """
      :type n: int
      :rtype: int
      """
      if n == 1:
          return 1
      # Initialize base cases
      first, second = 1, 2

      # Iterate from step 3 to n and calculate ways for each step
      for i in range(3, n + 1):
          current = first + second  # ways(i) = ways(i-1) + ways(i-2)
          first, second = second, current  # Update for the next iteration

      return second  # The number of ways to reach the top is stored in 'second'