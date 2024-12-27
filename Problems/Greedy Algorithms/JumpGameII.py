# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

class Solution:
  def jump(self, nums):
      n = len(nums)
      if n <= 1:
          return 0  # No jump needed if there's one or no element

      jumps = 0
      farthest = 0
      end_of_current_jump = 0

      for i in range(n):
          farthest = max(farthest, i + nums[i])  # Update farthest reachable index

          if i == end_of_current_jump:  # If we have reached the end of the current jump
              jumps += 1
              end_of_current_jump = farthest  # Set the end of the next jump

              if end_of_current_jump >= n - 1:  # If we can reach the last index
                  break

      return jumps