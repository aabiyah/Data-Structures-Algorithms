# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

class Solution(object):
# Using Two Pointers
    def removeDuplicates(self, nums):
        # Handling empty array
        if not nums:
            return 0

        # Initialize the slow pointer
        slow = 0 

        # Using fast pointer to iterate through array
        for fast in range (1, len(nums)):
            # If slow pointer and fast pointer are not equal, update the slow pointer value with the fast one to bring it forward and move the slow pointer one     element ahead
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1

