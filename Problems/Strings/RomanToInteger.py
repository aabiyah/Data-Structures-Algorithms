class Solution(object):
  def romanToInt(self, s):
      value_map = {
          'I': 1,
          'V': 5,
          'X': 10,
          'L': 50,
          'C': 100,
          'D': 500,
          'M': 1000
      }
      total = 0

      for i in range(len(s)):
          if i < len(s) - 1 and value_map[s[i]] < value_map[s[i+1]]:
              total -= value_map[s[i]]
          else:
              total += value_map[s[i]]
      return total