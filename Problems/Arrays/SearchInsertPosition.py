# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.

# To get O(log n) time complexity, we use Binary Search
class Solution(object):
  def searchInsert(self, nums, target):
      left, right = 0, len(nums) - 1

      while left <= right:
          mid = (left + right) // 2

          if nums[mid] == target:
              return mid  # Target found

          elif nums[mid] < target:
              left = mid + 1  # Search right half

          else:
              right = mid - 1  # Search left half

      # Target not found, return the insertion point
      return left
