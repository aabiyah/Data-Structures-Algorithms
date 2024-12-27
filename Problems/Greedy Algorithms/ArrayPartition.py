# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

class Solution:
  def arrayPairSum(self, nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      # Step 1: Sort the array
      nums.sort()

      # Step 2: Sum the elements at even indices (these will be the min of each pair)
      return sum(nums[i] for i in range(0, len(nums), 2))