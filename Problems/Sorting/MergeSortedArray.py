# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution:
  def merge(self, nums1, m, nums2, n):
      """
      :type nums1: List[int]
      :type m: int
      :type nums2: List[int]
      :type n: int
      :rtype: None Do not return anything, modify nums1 in-place instead.
      """
      # Pointers for nums1 and nums2
      p1 = m - 1
      p2 = n - 1
      # Pointer for the last position in nums1
      p = m + n - 1

      # Merge nums1 and nums2 from the back
      while p1 >= 0 and p2 >= 0:
          if nums1[p1] > nums2[p2]:
              nums1[p] = nums1[p1]
              p1 -= 1
          else:
              nums1[p] = nums2[p2]
              p2 -= 1
          p -= 1

      # If there are remaining elements in nums2, copy them
      while p2 >= 0:
          nums1[p] = nums2[p2]
          p2 -= 1
          p -= 1
