# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution(object):
  def maxSubArray(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      # Initialize variables to keep track of the maximum sum
      max_sum = nums[0]  # Maximum sum found so far
      current_sum = nums[0]  # Current subarray sum

      # Iterate through the array starting from the second element
      for i in range(1, len(nums)):
          # Either continue the subarray or start a new subarray with nums[i]
          current_sum = max(nums[i], current_sum + nums[i])
          # Update the maximum sum found so far
          max_sum = max(max_sum, current_sum)

      return max_sum