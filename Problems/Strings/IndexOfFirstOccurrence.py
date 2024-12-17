# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Example 1:
    # Input: haystack = "sadbutsad", needle = "sad"
    # Output: 0
    # Explanation: "sad" occurs at index 0 and 6.
    # The first occurrence is at index 0, so we return 0.

class Solution(object):
  def strStr(self, haystack, needle):
      if not needle:
          return 0
      m, n = len(haystack), len(needle)

      for i in range (m - n + 1):
          # Check if substring starting at i matches needle
          for j in range(n):
              if haystack[i+j] != needle[j]:
                  break
          else:
              # If loop completes without breaking, match is found
              return i
      # If no match is found
      return -1
