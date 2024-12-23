# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

  # Each row must contain the digits 1-9 without repetition.
  # Each column must contain the digits 1-9 without repetition.
  # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
  # A Sudoku board (partially filled) could be valid but is not necessarily solvable.
  # Only the filled cells need to be validated according to the mentioned rules.

class Solution(object):
  def isValidSudoku(self, board):
      """
      :type board: List[List[str]]
      :rtype: bool
      """
      # 9 sets for rows, columns and subgrids
      rows = [set() for _ in range(9)]
      cols = [set() for _ in range(9)]
      subgrids = [set() for _ in range(9)]

      for i in range(9):
          for j in range(9):
              num = board[i][j]
              if num != '.':  # Ignore empty cells
                  # Check row
                  if num in rows[i]:
                      return False
                  rows[i].add(num)

                  # Check column
                  if num in cols[j]:
                      return False
                  cols[j].add(num)

                  # Check subgrid
                  subgrid_index = (i // 3) * 3 + (j // 3)
                  if num in subgrids[subgrid_index]:
                      return False
                  subgrids[subgrid_index].add(num)

      return True
