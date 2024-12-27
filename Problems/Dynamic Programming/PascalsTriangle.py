# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

class Solution(object):
  def generate(self, numRows):
      """
      :type numRows: int
      :rtype: List[List[int]]
      """
      # Initialize the triangle with an empty list
      triangle = []

      # Iterate to generate each row
      for i in range(numRows):
          row = [1] * (i + 1)  # Initialize row with 1's

          # Fill in the interior elements (not the first and last)
          for j in range(1, i):
              row[j] = triangle[i-1][j-1] + triangle[i-1][j]

          # Add the current row to the triangle
          triangle.append(row)

      return triangle