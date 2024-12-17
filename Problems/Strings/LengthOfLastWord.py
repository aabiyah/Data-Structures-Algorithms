# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

class Solution(object):
  def lengthOfLastWord(self, s):
    # Strip trailing spaces and split the string into words
    words = s.strip().split()
    return len(words[-1]) if words else 0