# You are given an integer array nums and two integers indexDiff and valueDiff.

# Find a pair of indices (i, j) such that:
  # i != j,
  # abs(i - j) <= indexDiff.
  # abs(nums[i] - nums[j]) <= valueDiff, and
# Return true if such pair exists or false otherwise.

class Solution:
  def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
      if indexDiff <= 0 or valueDiff < 0:
          return False

      # Create a helper function to map a number to a bucket
      def get_bucket_key(num, width):
          # Use integer division to map the number to a bucket
          if num < 0:
              return (num + 1) // width - 1
          return num // width

      bucket_map = {}
      width = valueDiff + 1  # The width of each bucket

      for i, num in enumerate(nums):
          bucket_key = get_bucket_key(num, width)

          # Check if the current number is already in the same bucket
          if bucket_key in bucket_map:
              return True

          # Check the left adjacent bucket
          if bucket_key - 1 in bucket_map and num - bucket_map[bucket_key - 1] < width:
              return True

          # Check the right adjacent bucket
          if bucket_key + 1 in bucket_map and bucket_map[bucket_key + 1] - num < width:
              return True

          # Add the current number to the bucket map
          bucket_map[bucket_key] = num

          # Remove the number that is out of the sliding window
          if i >= indexDiff:
              del bucket_map[get_bucket_key(nums[i - indexDiff], width)]

      return False
