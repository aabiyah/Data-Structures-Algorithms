# Given a string s, find the length of the longest substring without repeating characters.

class Solution(object):
  def lengthOfLongestSubstring(self, s):
      char_set = set()  # To store unique characters in the current window
      left = 0  # Left pointer of the window
      max_length = 0  # To track the maximum length of a unique substring

      for right in range(len(s)):
          # If the character at 'right' is in the set, shrink the window
          while s[right] in char_set:
              char_set.remove(s[left])  # Remove the leftmost character
              left += 1  # Move the left pointer

          # Add the current character to the set and update max_length
          char_set.add(s[right])
          max_length = max(max_length, right - left + 1)

      return max_length

