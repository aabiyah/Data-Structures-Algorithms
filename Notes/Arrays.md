
# Arrays & Solving LeetCode Questions

## Basics of Arrays:
1. **Definition**: A data structure to store elements of the same type in contiguous memory.
2. **Indexing**: Access elements using `array[index]`. Zero-based indexing is common.
3. **Key Operations**:
   - Access: `O(1)`
   - Update: `O(1)`
   - Insert/Delete:
     - Start/End: `O(1)`
     - Middle: `O(n)` (requires shifting elements)

---

## Steps to Solve Array Problems:
1. **Understand the Problem**:
   - Read carefully, identify inputs/outputs.
   - Check constraints (e.g., array size, element range).

2. **Think Through Examples**:
   - Use small arrays as test cases.
   - Manually compute expected outputs.

3. **Choose an Approach**:
   - **Brute Force**: Iterate through all possibilities (useful to start).
   - **Optimize**: Identify patterns, use hash maps, sliding window, etc.

4. **Write Code**:
   - Use clear variable names and comments.
   - Handle edge cases (e.g., empty array, single element).

5. **Test**:
   - Test with provided examples.
   - Add edge cases and large inputs.

---

## Common Techniques:
1. **Two Pointers**:
   - Use for problems involving sorted arrays, subarrays, or partitions.
   - Example: Find pair with sum `target` in a sorted array.

2. **Sliding Window**:
   - Use for subarray problems (fixed/variable size).
   - Example: Maximum sum of subarray of size `k`.

3. **Hash Map**:
   - Store values or indices for quick lookups.
   - Example: Two Sum (find indices of two numbers adding to `target`).

4. **Sorting**:
   - Sort array to simplify conditions.
   - Example: Find unique triplets with a specific sum.

5. **Prefix Sum**:
   - Use for cumulative computations.
   - Example: Sum of subarray in `O(1)`.

6. **Binary Search**:
   - Use for sorted arrays.
   - Example: Find target in rotated sorted array.

---

## Example LeetCode Questions:
1. **Two Sum**:
   - Approach: Use a hash map for `O(n)` solution.

2. **Maximum Subarray (Kadane's Algorithm)**:
   - Track `currentSum` and `maxSum` for `O(n)` solution.

3. **Merge Intervals**:
   - Sort intervals and merge overlapping ones.

4. **Product of Array Except Self**:
   - Use prefix and suffix products for `O(n)` without extra division.

5. **Container With Most Water**:
   - Use two pointers to maximize area.

---

## Tips:
- **Practice Patterns**: Focus on recurring techniques like two pointers, sliding window.
- **Time Complexity**: Always analyze and optimize.
- **Edge Cases**: Think about empty arrays, negative numbers, duplicates, etc.
- **Debugging**: Use print statements for tricky parts.

---

Keep practicing small, focused problems to build confidence!
