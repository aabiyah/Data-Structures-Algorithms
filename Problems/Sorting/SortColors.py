# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

class Solution:
  def sortColors(self, nums):
      """
      :type nums: List[int]
      :rtype: None (Do not return anything, modify nums in-place instead.)
      """
      low, mid, high = 0, 0, len(nums) - 1

      while mid <= high:
          if nums[mid] == 0:
              # Swap nums[low] and nums[mid]
              nums[low], nums[mid] = nums[mid], nums[low]
              low += 1
              mid += 1
          elif nums[mid] == 1:
              # Leave 1 in place
              mid += 1
          else:  # nums[mid] == 2
              # Swap nums[mid] and nums[high]
              nums[mid], nums[high] = nums[high], nums[mid]
              high -= 1