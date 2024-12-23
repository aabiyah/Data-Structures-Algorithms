# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

class Solution(object):
  def groupAnagrams(self, strs):
      """
      :type strs: List[str]
      :rtype: List[List[str]]
      """
      anagrams = defaultdict(list)

      for s in strs:
          sorted_str = ''.join(sorted(s))  # Sort the string and use as key
          anagrams[sorted_str].append(s)   # Append the original string to the list

      return list(anagrams.values())  # Return the grouped anagrams as a list of lists
