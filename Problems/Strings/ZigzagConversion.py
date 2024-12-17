# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

class Solution(object):
  def convert(self, s, numRows):
      # Edge case: If numRows is 1 or the string length is less than numRows, return the string as is
      if numRows == 1 or numRows >= len(s):
          return s

      # Create a list of strings to represent rows
      rows = [""] * numRows
      current_row = 0
      direction = 1  # 1 for down, -1 for up

      # Traverse the string
      for char in s:
          rows[current_row] += char  # Add the character to the current row

          # Change direction if we hit the top or bottom row
          if current_row == 0:
              direction = 1  # Start moving down
          elif current_row == numRows - 1:
              direction = -1  # Start moving up

          # Move to the next row
          current_row += direction

      # Combine all rows to form the final zigzag string
      return "".join(rows)
