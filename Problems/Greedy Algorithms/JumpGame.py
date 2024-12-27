# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

class Solution:
  def canJump(self, nums):
      farthest = 0
      for i in range(len(nums)):
          if i > farthest:  # If i is beyond the farthest reachable index
              return False
          farthest = max(farthest, i + nums[i])  # Update the farthest index we can reach
          if farthest >= len(nums) - 1:  # If we can reach the last index
              return True
      return False