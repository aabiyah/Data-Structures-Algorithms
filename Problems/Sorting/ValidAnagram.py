# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution(object):
  def isAnagram(self, s, t):
      """
      :type s: str
      :type t: str
      :rtype: bool
      """
      return Counter(s) == Counter(t)