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
        # Initialize constraints
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrids = [set() for _ in range(9)]
        empty_cells = []

        # Helper function to get subgrid index
        def get_subgrid_index(row, col):
            return (row // 3) * 3 + (col // 3)

        # Populate constraints and identify empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    subgrids[get_subgrid_index(r, c)].add(num)

        # Backtracking function
        def backtrack(index):
            # If we processed all empty cells, the board is solved
            if index == len(empty_cells):
                return True

            # Get the current empty cell
            row, col = empty_cells[index]
            subgrid_index = get_subgrid_index(row, col)

            # Try placing numbers 1-9
            for num in '123456789':
                if num not in rows[row] and num not in cols[col] and num not in subgrids[subgrid_index]:
                    # Place the number and update constraints
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    subgrids[subgrid_index].add(num)

                    # Recur for the next empty cell
                    if backtrack(index + 1):
                        return True

                    # Undo the move (backtrack)
                    board[row][col] = '.'
                    rows[row].remove(num)
                    cols[col].remove(num)
                    subgrids[subgrid_index].remove(num)

            # If no valid number can be placed, return False
            return False

        # Start solving from the first empty cell
        backtrack(0)
