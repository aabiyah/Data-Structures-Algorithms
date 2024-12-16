# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

class Solution(object):
  def removeElement(self, nums, val):
      slow = 0

      # Traverse the array with the fast pointer
      for fast in range(len(nums)):
          # If the current element is not equal to val
          if nums[fast] != val:
              # Copy it to the position of slow pointer
              nums[slow] = nums[fast]
              slow += 1

      # Return the count of elements not equal to val
      return slow