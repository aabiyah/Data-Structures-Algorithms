
# Sorting & Solving LeetCode Questions

## Basics of Sorting:
1. **Definition**: Sorting rearranges elements of a list/array in a specific order (ascending or descending).
2. **Key Metrics**:
   - **Time Complexity**: How fast the algorithm sorts (e.g., `O(n log n)`).
   - **Space Complexity**: Additional memory required.
   - **Stability**: Maintains the relative order of equal elements.

---

## Common Sorting Algorithms:

### 1. **Bubble Sort**:
   - **Idea**: Repeatedly swap adjacent elements if they are in the wrong order.
   - **Time Complexity**: `O(n^2)`
   - **Space Complexity**: `O(1)`
   - **Use Case**: Simple, but rarely used in practice.

### 2. **Selection Sort**:
   - **Idea**: Find the smallest element and place it in its correct position.
   - **Time Complexity**: `O(n^2)`
   - **Space Complexity**: `O(1)`
   - **Use Case**: Useful for small datasets.

### 3. **Insertion Sort**:
   - **Idea**: Build a sorted array one element at a time by inserting in the correct position.
   - **Time Complexity**: `O(n^2)` (best case: `O(n)` for nearly sorted data)
   - **Space Complexity**: `O(1)`
   - **Use Case**: Efficient for small or partially sorted arrays.

### 4. **Merge Sort**:
   - **Idea**: Divide the array into halves, sort each half, and merge them.
   - **Time Complexity**: `O(n log n)`
   - **Space Complexity**: `O(n)`
   - **Use Case**: Stable and works well with linked lists.

### 5. **Quick Sort**:
   - **Idea**: Choose a pivot, partition the array, and recursively sort subarrays.
   - **Time Complexity**: `O(n log n)` (worst case: `O(n^2)`)
   - **Space Complexity**: `O(log n)` (in-place)
   - **Use Case**: Fast and widely used in practice.

### 6. **Heap Sort**:
   - **Idea**: Use a heap data structure to repeatedly extract the maximum/minimum.
   - **Time Complexity**: `O(n log n)`
   - **Space Complexity**: `O(1)`
   - **Use Case**: In-place but not stable.

### 7. **Counting Sort**:
   - **Idea**: Count occurrences of elements and place them in sorted order.
   - **Time Complexity**: `O(n + k)` (where `k` is the range of input values)
   - **Space Complexity**: `O(k)`
   - **Use Case**: Efficient for small ranges of integers.

### 8. **Radix Sort**:
   - **Idea**: Sort elements digit by digit using counting sort as a subroutine.
   - **Time Complexity**: `O(nk)` (where `k` is the number of digits)
   - **Space Complexity**: `O(n + k)`
   - **Use Case**: Works well for integers and strings.

### 9. **Bucket Sort**:
   - **Idea**: Divide elements into buckets, sort each bucket, and combine them.
   - **Time Complexity**: `O(n + k)` (average case)
   - **Space Complexity**: `O(n + k)`
   - **Use Case**: Efficient for uniformly distributed data.

---

## Steps to Solve Sorting Problems:
1. **Understand the Problem**:
   - Identify the desired order (ascending, descending, custom).
   - Check constraints (e.g., input size, duplicates).

2. **Choose the Algorithm**:
   - Small Input: Insertion or Selection Sort.
   - Large Input: Merge, Quick, or Heap Sort.
   - Integers with Small Range: Counting or Radix Sort.

3. **Implement**:
   - Use built-in sorting functions if applicable.
   - For custom orders, use a comparator or key function.

4. **Test**:
   - Test with edge cases like empty arrays, duplicates, and sorted arrays.

---

## Example LeetCode Questions:
1. **Sort Colors**:
   - Use a variant of counting sort or two pointers.

2. **Kth Largest Element**:
   - Use quickselect (a variant of quicksort).

3. **Merge Intervals**:
   - Sort intervals by start time and merge overlapping ones.

4. **Top K Frequent Elements**:
   - Use a heap or bucket sort.

5. **Largest Number**:
   - Sort numbers as strings using a custom comparator.

6. **Meeting Rooms II**:
   - Sort intervals and use a min-heap to track rooms.

---

## Tips:
- **Built-In Sorts**: Use `sorted()` in Python (Timsort, `O(n log n)`).
- **Stability**: Use stable sorts if required by the problem.
- **Time Complexity**: Aim for `O(n log n)` for large inputs.
- **Edge Cases**: Test with empty arrays, single elements, and duplicates.

---

Master sorting algorithms to enhance problem-solving efficiency!
