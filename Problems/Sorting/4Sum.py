# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

class Solution:
  def fourSum(self, nums, target):
      """
      :type nums: List[int]
      :type target: int
      :rtype: List[List[int]]
      """
      nums.sort()  # Sort the array
      n = len(nums)
      result = []

      # Iterate through the array to fix the first number
      for i in range(n - 3):
          # Avoid duplicates for the first number
          if i > 0 and nums[i] == nums[i - 1]:
              continue

          # Iterate to fix the second number
          for j in range(i + 1, n - 2):
              # Avoid duplicates for the second number
              if j > i + 1 and nums[j] == nums[j - 1]:
                  continue

              # Two pointers for the remaining two numbers
              left, right = j + 1, n - 1
              while left < right:
                  total = nums[i] + nums[j] + nums[left] + nums[right]

                  if total == target:
                      result.append([nums[i], nums[j], nums[left], nums[right]])

                      # Skip duplicates for the third number
                      while left < right and nums[left] == nums[left + 1]:
                          left += 1
                      # Skip duplicates for the fourth number
                      while left < right and nums[right] == nums[right - 1]:
                          right -= 1

                      left += 1
                      right -= 1
                  elif total < target:
                      left += 1
                  else:
                      right -= 1

      return result