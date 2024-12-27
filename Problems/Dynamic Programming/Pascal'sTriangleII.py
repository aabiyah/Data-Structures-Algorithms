# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution(object):
  def getRow(self, rowIndex):
      """
      :type rowIndex: int
      :rtype: List[int]
      """
      # Start with the first row [1]
      row = [1]

      # Iterate through to build each row up to rowIndex
      for i in range(1, rowIndex + 1):
          # Build the next row based on the previous one
          # We add 1 at the start, then compute each element in the middle
          # Then add 1 at the end.
          new_row = [1] * (i + 1)
          for j in range(1, i):
              new_row[j] = row[j - 1] + row[j]
          row = new_row  # Move to the next row

      return row