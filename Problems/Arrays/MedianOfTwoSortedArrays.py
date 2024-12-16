# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):

      # Ensure nums1 is the smaller array
      if len(nums1) > len(nums2):
          nums1, nums2 = nums2, nums1

      m, n = len(nums1), len(nums2)
      left, right = 0, m

      while left <= right:
          partition1 = (left + right) // 2
          partition2 = (m + n + 1) // 2 - partition1

          # Handle edge cases for maxLeft and minRight
          maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
          minRight1 = float('inf') if partition1 == m else nums1[partition1]

          maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
          minRight2 = float('inf') if partition2 == n else nums2[partition2]

          # Check if the partition is correct
          if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
              # Found the correct partition
              if (m + n) % 2 == 0:
                  # Even total elements
                  return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
              else:
                  # Odd total elements
                  return max(maxLeft1, maxLeft2)
          elif maxLeft1 > minRight2:
              # Move partition1 to the left
              right = partition1 - 1
          else:
              # Move partition1 to the right
              left = partition1 + 1

      raise ValueError("Input arrays are not valid")
