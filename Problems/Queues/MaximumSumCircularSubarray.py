# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

class Solution:
  def maxSubarraySumCircular(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      # Helper function to find the max or min subarray sum
      def kadane(nums, find_max=True):
          curr = best = nums[0]
          for num in nums[1:]:
              if find_max:
                  curr = max(num, curr + num)
                  best = max(best, curr)
              else:
                  curr = min(num, curr + num)
                  best = min(best, curr)
          return best

      # Step 1: Find the normal max subarray sum (Kadane's)
      max_normal = kadane(nums, find_max=True)

      # Step 2: Find the circular max subarray sum
      total_sum = sum(nums)
      min_subarray_sum = kadane(nums, find_max=False)
      max_circular = total_sum - min_subarray_sum

      # Step 3: Handle the edge case where all elements are negative
      if max_normal < 0:  # All elements are negative
          return max_normal

      # Step 4: Return the maximum of the two cases
      return max(max_normal, max_circular)