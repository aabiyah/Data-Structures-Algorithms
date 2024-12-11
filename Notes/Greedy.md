
# Greedy Algorithms & Solving LeetCode Questions

## Basics of Greedy Algorithms:
1. **Definition**: A strategy that makes the optimal choice at each step, assuming it leads to the global optimum.
2. **Key Characteristics**:
   - **Greedy Choice Property**: A global solution can be built by making locally optimal choices.
   - **Optimal Substructure**: A solution to a problem can be constructed from solutions to its subproblems.
3. **Applications**:
   - Scheduling, interval problems, minimum spanning trees, and resource allocation.

---

## Steps to Solve Greedy Problems:
1. **Understand the Problem**:
   - Identify if a greedy approach is feasible (check properties above).
   - Analyze constraints and goals (e.g., minimize/maximize a metric).

2. **Sort/Preprocess the Data**:
   - Sorting often helps to simplify greedy choices.

3. **Choose the Greedy Strategy**:
   - Define the locally optimal choice (e.g., shortest, largest, earliest).

4. **Write Code**:
   - Implement the greedy decision-making process iteratively.
   - Use auxiliary structures (e.g., priority queues) if needed.

5. **Test**:
   - Test with examples to ensure correctness.
   - Add edge cases (e.g., smallest/largest inputs).

---

## Common Techniques:
1. **Activity Selection**:
   - Sort activities by end time and select non-overlapping ones.
   - Example: Maximum number of meetings in one room.

2. **Interval Scheduling**:
   - Use sorting and greedy selection for start/end times.
   - Example: Merge overlapping intervals.

3. **Huffman Encoding**:
   - Build a frequency-based tree for optimal encoding.

4. **Minimum Spanning Tree**:
   - Use Prim’s or Kruskal’s algorithm with greedy choices.

5. **Knapsack Problem (Fractional)**:
   - Sort items by value/weight ratio and take as much as possible.
   - Note: Works for fractional, not 0/1 knapsack.

6. **Dijkstra's Algorithm**:
   - Use greedy selection to find the shortest path in weighted graphs.

7. **Resource Allocation**:
   - Allocate resources to maximize or minimize usage.
   - Example: Assigning tasks to workers.

---

## Example LeetCode Questions:
1. **Minimum Number of Platforms**:
   - Use sorting and greedy allocation of platforms.

2. **Candy Distribution**:
   - Use two passes to distribute candies based on ratings.

3. **Partition Labels**:
   - Divide the string into partitions using the last occurrence of characters.

4. **Gas Station**:
   - Use a greedy approach to find the starting point for completing the circuit.

5. **Jump Game II**:
   - Use a greedy approach to minimize jumps to reach the end.

6. **Task Scheduler**:
   - Use greedy scheduling to minimize idle time.

7. **Greedy Florist**:
   - Minimize cost by buying expensive flowers first.

---

## Tips:
- **Feasibility**: Verify that the problem satisfies greedy properties.
- **Sort First**: Many greedy problems require initial sorting.
- **Edge Cases**: Handle single element inputs, empty inputs, and boundary conditions.
- **Time Complexity**: Aim for efficient greedy operations (`O(n log n)` or better).
- **Debugging**: Print greedy decisions step-by-step to verify correctness.

---

Practice greedy algorithms to excel in solving optimization and scheduling problems efficiently!
