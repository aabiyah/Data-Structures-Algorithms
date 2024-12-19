# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

class Solution:
  def maxSubarraySumCircular(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      # Helper function for Kadane's algorithm
      def kadane(nums):
          max_current = max_global = nums[0]
          for num in nums[1:]:
              max_current = max(num, max_current + num)
              max_global = max(max_global, max_current)
          return max_global

      # Calculate the total sum of the array
      total_sum = sum(nums)

      # Find the maximum subarray sum using Kadane's algorithm
      max_sum = kadane(nums)

      # Find the minimum subarray sum using Kadane's algorithm (on negative nums)
      min_current = min_global = nums[0]
      for num in nums[1:]:
          min_current = min(num, min_current + num)
          min_global = min(min_global, min_current)
      min_sum = min_global

      # Handle the edge case where all numbers are negative
      if max_sum < 0:
          return max_sum

      # Return the maximum of the linear and circular cases
      return max(max_sum, total_sum - min_sum)
