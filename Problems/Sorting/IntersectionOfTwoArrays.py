# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

class Solution:
  def intersection(self, nums1, nums2):
      """
      :type nums1: List[int]
      :type nums2: List[int]
      :rtype: List[int]
      """
      nums1.sort()
      nums2.sort()
      i, j = 0, 0
      result = set()

      while i < len(nums1) and j < len(nums2):
          if nums1[i] == nums2[j]:
              result.add(nums1[i])
              i += 1
              j += 1
          elif nums1[i] < nums2[j]:
              i += 1
          else:
              j += 1

      return list(result)