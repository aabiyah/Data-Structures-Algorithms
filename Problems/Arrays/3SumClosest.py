# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

class Solution(object):
  def threeSumClosest(self, nums, target):
      # Step 1: Sort the array
      nums.sort()
      closest_sum = float('inf')  # Initialize closest sum to infinity

      # Step 2: Iterate through the array
      for i in range(len(nums)):
          left = i + 1
          right = len(nums) - 1

          # Step 3: Use two pointers to find the closest sum
          while left < right:
              current_sum = nums[i] + nums[left] + nums[right]

              # Update the closest sum if needed
              if abs(current_sum - target) < abs(closest_sum - target):
                  closest_sum = current_sum

              # If the current sum equals the target, return immediately
              if current_sum == target:
                  return current_sum

              # Adjust pointers based on the comparison
              if current_sum < target:
                  left += 1
              else:
                  right -= 1

      # Step 4: Return the closest sum
      return closest_sum
