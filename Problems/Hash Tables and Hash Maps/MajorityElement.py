# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution:
  def majorityElement(self, nums):
      # Step 1: Initialize variables
      candidate = None
      count = 0

      # Step 2: Iterate through the list
      for num in nums:
          if count == 0:
              candidate = num  # Choose the new candidate
          count += (1 if num == candidate else -1)  # Increment or decrement the count

      # Step 3: Return the candidate (it is guaranteed to be the majority element)
      return candidate