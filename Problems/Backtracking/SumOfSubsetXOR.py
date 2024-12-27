# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# Given an array nums, return the sum of all XOR totals for every subset of nums. 

# Note: Subsets with the same elements should be counted multiple times.

# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

class Solution:
  def subsetXORSum(self, nums):
      result = 0

      # Iterate over each number in the array
      for num in nums:
          result |= num  # Apply the OR operation to accumulate the XOR sum

      # The number of subsets of nums is 2^n.
      # Each element contributes in exactly half of the subsets, hence multiply result by 2^(n-1)
      return result * (1 << len(nums) - 1)
