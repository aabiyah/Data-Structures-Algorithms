
# Backtracking & Solving LeetCode Questions

## Basics of Backtracking:
1. **Definition**: A systematic way to explore all possibilities by building a solution incrementally and backtracking when constraints are violated.
2. **Key Characteristics**:
   - **Recursive Exploration**: Use recursion to explore solutions step-by-step.
   - **Constraint Checking**: Stop exploring a branch if it violates constraints.
   - **Undoing Choices**: Backtrack by undoing the last decision and trying the next one.
3. **Applications**:
   - Permutations, combinations, subset generation, and solving puzzles (e.g., Sudoku, N-Queens).

---

## Steps to Solve Backtracking Problems:
1. **Understand the Problem**:
   - Identify if the problem involves exploring multiple possibilities.
   - Define the constraints and goals.

2. **Choose the State Representation**:
   - Determine how to represent the solution state (e.g., arrays, lists, sets).

3. **Write a Recursive Function**:
   - Base Case: Define when to stop recursion (e.g., a valid solution is found).
   - Recursive Case: Try all possibilities and backtrack when necessary.

4. **Prune Unnecessary Branches**:
   - Use constraints to eliminate invalid branches early.

5. **Test**:
   - Test with small inputs to validate constraints and backtracking logic.
   - Add edge cases (e.g., smallest or largest inputs).

---

## Common Techniques:
1. **Generate All Combinations/Permutations**:
   - Use recursion to explore all possible arrangements.
   - Example: Generate all permutations of an array.

2. **Solve Puzzles**:
   - Explore all possibilities and backtrack if constraints are violated.
   - Example: Solve Sudoku or N-Queens.

3. **Subset Generation**:
   - Use recursion to include or exclude each element.
   - Example: Find all subsets of a set.

4. **Pathfinding with Constraints**:
   - Explore paths in a graph or grid, backtracking when a path is invalid.
   - Example: Word search in a 2D grid.

5. **Optimized Backtracking**:
   - Use additional data structures to track visited states or prune branches.
   - Example: Check for duplicate subsets using hash sets.

---

## Example LeetCode Questions:
1. **Permutations**:
   - Use recursion to generate all permutations of a list.

2. **Combination Sum**:
   - Use backtracking to find all combinations that sum to a target.

3. **N-Queens**:
   - Use recursion and backtracking to place queens without conflict.

4. **Word Search**:
   - Explore all paths in a grid recursively to find a word.

5. **Generate Parentheses**:
   - Use backtracking to generate all valid combinations.

6. **Palindrome Partitioning**:
   - Use backtracking to partition strings into palindromic substrings.

7. **Sudoku Solver**:
   - Use backtracking to fill in a Sudoku board.

---

## Tips:
- **Base Case**: Clearly define stopping conditions to avoid infinite recursion.
- **Constraint Pruning**: Eliminate invalid branches early for efficiency.
- **Undo Changes**: Remember to undo changes when backtracking.
- **Time Complexity**: Analyze the total number of recursive calls and constraints.
- **Debugging**: Use print statements to trace recursive calls and backtracking steps.

---

Master backtracking to solve problems involving permutations, combinations, and constraint satisfaction efficiently!
