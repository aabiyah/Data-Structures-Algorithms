# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.

class Solution(object):
  def threeSum(self, nums):
      # Step 1: Sort the array
      nums.sort()
      result = []

      # Step 2: Iterate through the array
      for i in range(len(nums)):
          # Skip duplicate elements for the fixed number
          if i > 0 and nums[i] == nums[i - 1]:
              continue

          # Step 3: Use two pointers to find the remaining two numbers
          left = i + 1
          right = len(nums) - 1

          while left < right:
              total = nums[i] + nums[left] + nums[right]

              if total == 0:
                  # Add the triplet to the result
                  result.append([nums[i], nums[left], nums[right]])

                  # Skip duplicates for left and right pointers
                  while left < right and nums[left] == nums[left + 1]:
                      left += 1
                  while left < right and nums[right] == nums[right - 1]:
                      right -= 1

                  # Move both pointers inward
                  left += 1
                  right -= 1

              elif total < 0:
                  # Move the left pointer to increase the sum
                  left += 1
              else:
                  # Move the right pointer to decrease the sum
                  right -= 1

      return result
