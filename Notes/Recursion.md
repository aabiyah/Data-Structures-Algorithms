
# Recursion & Solving LeetCode Questions

## Basics of Recursion:
1. **Definition**: A function calls itself to solve smaller instances of the same problem.
2. **Key Components**:
   - **Base Case**: The condition that stops the recursion.
   - **Recursive Case**: The part of the function that reduces the problem and calls itself.
3. **Applications**:
   - Divide and conquer algorithms, backtracking, tree/graph traversal, and dynamic programming.

---

## Steps to Solve Recursive Problems:
1. **Understand the Problem**:
   - Identify if the problem can be broken into smaller subproblems.
   - Recognize patterns like repetitive structure or overlapping subproblems.

2. **Define Base and Recursive Cases**:
   - Clearly define the stopping condition (base case).
   - Write the recursive relation for subproblems.

3. **Write Code**:
   - Implement the function with the base case first.
   - Use recursion to solve the reduced problem.

4. **Test**:
   - Test with small inputs to validate base and recursive cases.
   - Add edge cases (e.g., smallest or largest inputs).

---

## Common Techniques:
1. **Factorial/Power Computation**:
   - Base Case: `n == 0 or 1`.
   - Recursive Case: `n * factorial(n-1)` or `x^n = x * power(x, n-1)`.

2. **Tree Traversal**:
   - Use recursion for preorder, inorder, and postorder traversals.

3. **Graph Traversal**:
   - DFS can be implemented recursively for connected components or paths.

4. **Backtracking**:
   - Use recursion to explore all possibilities.
   - Example: Solving mazes, N-Queens problem.

5. **Divide and Conquer**:
   - Split the problem into smaller subproblems and combine results.
   - Example: Merge sort, quick sort, binary search.

6. **Dynamic Programming**:
   - Use recursion with memoization to avoid redundant calculations.
   - Example: Fibonacci sequence, coin change.

---

## Example LeetCode Questions:
1. **Climbing Stairs**:
   - Use recursion with memoization to count paths.

2. **Generate Parentheses**:
   - Use backtracking with recursion to generate all valid combinations.

3. **Maximum Depth of Binary Tree**:
   - Use recursion to find the height of the left and right subtrees.

4. **Permutations**:
   - Use recursion to explore all permutations of an array.

5. **Subsets**:
   - Use recursion to generate all subsets.

6. **Word Search**:
   - Use backtracking with recursion to search for words in a grid.

7. **Merge Sort**:
   - Recursively divide the array and merge sorted halves.

---

## Tips:
- **Base Case**: Always define it clearly to avoid infinite recursion.
- **Time Complexity**: Analyze the number of recursive calls and the work done at each step.
- **Memoization**: Store results of subproblems to optimize overlapping calls.
- **Debugging**: Use print statements to track recursive calls and results.
- **Avoid Stack Overflow**: For large inputs, use iterative solutions or optimize recursion depth.

---

Master recursion to solve problems involving repetitive subproblems, hierarchical structures, and backtracking efficiently!
