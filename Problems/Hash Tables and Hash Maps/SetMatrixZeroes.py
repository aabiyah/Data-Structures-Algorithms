# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

class Solution(object):
  def setZeroes(self, matrix):
      """
      :type matrix: List[List[int]]
      :rtype: None Do not return anything, modify matrix in-place instead.
      """
      m, n = len(matrix), len(matrix[0])

      # Flags to check if the first row or first column should be zeroed
      first_row = any(matrix[0][j] == 0 for j in range(n))
      first_col = any(matrix[i][0] == 0 for i in range(m))

      # Use first row and first column to mark zero rows and columns
      for i in range(1, m):
          for j in range(1, n):
              if matrix[i][j] == 0:
                  matrix[i][0] = 0  # Mark the first column for row i
                  matrix[0][j] = 0  # Mark the first row for column j

      # Set the interior cells to 0 based on the marks in the first row and column
      for i in range(1, m):
          for j in range(1, n):
              if matrix[i][0] == 0 or matrix[0][j] == 0:
                  matrix[i][j] = 0

      # Finally, handle the first row and first column separately
      if first_row:
          for j in range(n):
              matrix[0][j] = 0

      if first_col:
          for i in range(m):
              matrix[i][0] = 0
