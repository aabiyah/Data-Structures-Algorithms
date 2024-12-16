# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def is_valid(row, col, num):
            # Check the row
            for c in range(9):
                if board[row][c] == num:
                    return False

            # Check the column
            for r in range(9):
                if board[r][col] == num:
                    return False

            # Check the 3x3 sub-grid
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    if board[r][c] == num:
                        return False

            return True

        def backtrack():
            # Find the next empty cell
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        # Try placing digits 1 to 9
                        for num in '123456789':
                            if is_valid(row, col, num):
                                # Place the number
                                board[row][col] = num
                                # Recur to solve the rest of the board
                                if backtrack():
                                    return True
                                # Undo the move (backtrack)
                                board[row][col] = '.'
                        return False
            # If no empty cells remain, the board is solved
            return True

        backtrack()

