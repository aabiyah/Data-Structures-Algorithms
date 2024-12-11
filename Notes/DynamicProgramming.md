
# Dynamic Programming & Solving LeetCode Questions

## Basics of Dynamic Programming (DP):
1. **Definition**: A technique to solve problems by breaking them into overlapping subproblems and storing results to avoid redundant calculations.
2. **Key Concepts**:
   - **Overlapping Subproblems**: Solve the same subproblem multiple times.
   - **Optimal Substructure**: An optimal solution to a problem can be built from optimal solutions of its subproblems.
   - **Memoization**: Store results of subproblems (top-down approach).
   - **Tabulation**: Build solutions iteratively in a table (bottom-up approach).
3. **Applications**:
   - Sequence alignment, pathfinding, knapsack problem, and partitioning.

---

## Steps to Solve DP Problems:
1. **Understand the Problem**:
   - Identify if the problem has overlapping subproblems and optimal substructure.
   - Define the problem state (parameters representing the subproblem).

2. **Define the State**:
   - Choose a way to represent subproblems (e.g., `dp[i]` or `dp[i][j]`).

3. **State Transition**:
   - Write a recurrence relation to compute `dp[i]` using smaller subproblems.

4. **Base Case**:
   - Identify the simplest case(s) and initialize the DP table accordingly.

5. **Choose a Strategy**:
   - **Top-Down**: Use recursion with memoization.
   - **Bottom-Up**: Fill a DP table iteratively.

6. **Test**:
   - Test with small inputs to ensure correct recurrence and base cases.
   - Add edge cases (e.g., smallest or largest inputs).

---

## Common Techniques:
1. **1D DP**:
   - Use a single array to represent states.
   - Example: Fibonacci, climbing stairs, maximum subarray.

2. **2D DP**:
   - Use a matrix for problems involving two parameters.
   - Example: Longest common subsequence, edit distance.

3. **Knapsack Problems**:
   - Solve using `dp[i][j]` to represent items and capacity.
   - Example: 0/1 knapsack, unbounded knapsack.

4. **DP on Strings**:
   - Use DP for alignment, transformation, or comparison.
   - Example: Longest palindromic subsequence, word break.

5. **DP on Trees**:
   - Use postorder traversal to compute DP values.
   - Example: Maximum path sum, robbing houses on a tree.

6. **Space Optimization**:
   - Reduce space complexity by keeping only the previous state(s).
   - Example: Fibonacci using two variables instead of an array.

---

## Example LeetCode Questions:
1. **Climbing Stairs**:
   - Use DP to count ways to reach the top.

2. **House Robber**:
   - Use DP to maximize the sum without robbing adjacent houses.

3. **Longest Increasing Subsequence**:
   - Use DP to find the length of the LIS.

4. **Coin Change**:
   - Use DP to find the minimum number of coins to make an amount.

5. **Longest Common Subsequence**:
   - Use 2D DP to find the LCS of two strings.

6. **Partition Equal Subset Sum**:
   - Use DP to check if a subset with half the total sum exists.

7. **Word Break**:
   - Use DP to check if a string can be segmented into valid words.

---

## Tips:
- **State Representation**: Clearly define the `dp` array or table.
- **Iterative vs Recursive**: Choose based on problem size and constraints.
- **Debugging**: Print the DP table to trace calculations.
- **Time Complexity**: Analyze based on state count and recurrence relation.
- **Space Optimization**: Use rolling arrays or variables when possible.

---

Master dynamic programming to solve problems involving optimization, sequences, and partitioning efficiently!
