# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

    class TwoSum(object):
    # Using Hashmap for better time complexity (O(n))
      def twoSum(self, nums, target):
          # Create a hashmap to store value -> index mapping
          hashmap = {}

          # Iterate through the list of numbers
          for i, num in enumerate(nums):
              # Calculate the complement
              complement = target - num

              # Check if complement exists in hashmap
              if complement in hashmap:
                  return [hashmap[complement], i]

              # Otherwise, add the current number to the hashmap
              hashmap[num] = i

