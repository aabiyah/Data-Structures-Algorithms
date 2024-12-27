# A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

# For example, the below binary watch reads "4:51".


# Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

# The hour must not contain a leading zero.

# For example, "01:00" is not valid. It should be "1:00".
# The minute must consist of two digits and may contain a leading zero.

# For example, "10:2" is not valid. It should be "10:02".

class Solution(object):
  def readBinaryWatch(self, turnedOn):
      result = []

      # Try all possible hours and minutes combinations
      for h in range(12):  # There are 12 possible hours: 0-11
          for m in range(60):  # There are 60 possible minutes: 0-59
              # Count the number of 1s in binary representations of hour and minute
              if bin(h).count('1') + bin(m).count('1') == turnedOn:
                  # If the sum of 1's in hour and minute matches turnedOn, we have a valid time
                  result.append("{}:{:02d}".format(h, m))  # Format minute with leading zero if necessary

      return result