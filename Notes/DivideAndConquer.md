
# Divide and Conquer & Solving LeetCode Questions

## Basics of Divide and Conquer:
1. **Definition**: A strategy that breaks a problem into smaller subproblems, solves them, and combines their solutions.
2. **Key Steps**:
   - **Divide**: Split the problem into smaller parts.
   - **Conquer**: Solve each subproblem recursively.
   - **Combine**: Merge the solutions of the subproblems.
3. **Applications**:
   - Sorting (Merge Sort, Quick Sort)
   - Searching (Binary Search)
   - Recursive algorithms (Tree traversal, Dynamic Programming)

---

## Steps to Solve Divide and Conquer Problems:
1. **Understand the Problem**:
   - Check if the problem can be divided into independent subproblems.
   - Identify the base case for recursion.

2. **Think Through Examples**:
   - Use small inputs to visualize the division and merging process.

3. **Choose an Approach**:
   - Recursively divide the input and process smaller pieces.
   - Use helper functions for clarity.

4. **Write Code**:
   - Handle the base case first.
   - Recurse for subproblems and merge results.

5. **Test**:
   - Test with provided examples.
   - Add edge cases (e.g., smallest inputs, large inputs).

---

## Common Techniques:
1. **Binary Search**:
   - Divide the search space in half each time.
   - Example: Find target in sorted array.

2. **Merge Sort**:
   - Divide the array into halves, sort each, and merge them.
   - Example: Sort an array.

3. **Quick Sort**:
   - Partition the array and sort subarrays recursively.
   - Example: Sort an array efficiently.

4. **Maximum Subarray (Kadane's Variant)**:
   - Divide the array into halves and find the max subarray crossing the middle.
   - Example: Find maximum subarray sum.

5. **Matrix Multiplication**:
   - Divide matrices into submatrices.
   - Example: Strassen’s algorithm.

6. **Closest Pair of Points**:
   - Divide points by coordinates and solve recursively.
   - Example: Find closest two points in a plane.

7. **Tree-Based Problems**:
   - Solve subtrees recursively and merge results.
   - Example: Maximum path sum in a binary tree.

---

## Example LeetCode Questions:
1. **Binary Search**:
   - Divide the array in half to find the target.

2. **Sort an Array**:
   - Use merge sort or quick sort.

3. **Maximum Subarray**:
   - Use divide and conquer to find the maximum subarray sum.

4. **Kth Largest Element in an Array**:
   - Use quickselect (variant of quick sort).

5. **Pow(x, n)**:
   - Divide the power calculation recursively.

6. **Different Ways to Add Parentheses**:
   - Divide the expression at each operator.

---

## Tips:
- **Base Case**: Ensure a clear stopping condition to avoid infinite recursion.
- **Combine Step**: Be mindful of how subproblems are merged.
- **Time Complexity**: Analyze recursion depth and merging cost (e.g., `O(n log n)` for merge sort).
- **Edge Cases**: Consider single-element inputs and empty inputs.
- **Debugging**: Print intermediate results to verify recursion logic.

---

Master divide and conquer to solve complex problems efficiently!
