
# Queues & Solving LeetCode Questions

## Basics of Queues:
1. **Definition**: A linear data structure following the **FIFO** (First In, First Out) principle.
2. **Key Operations**:
   - **Enqueue**: Add an element to the end of the queue. `O(1)`
   - **Dequeue**: Remove an element from the front. `O(1)`
   - **Peek/Front**: Access the front element without removing it. `O(1)`
   - **Is Empty**: Check if the queue is empty. `O(1)`

---

## Steps to Solve Queue Problems:
1. **Understand the Problem**:
   - Identify operations needed (enqueue, dequeue, etc.).
   - Check constraints (e.g., queue size, input format).

2. **Think Through Examples**:
   - Use small examples to simulate queue operations manually.

3. **Choose an Approach**:
   - Use `collections.deque` for queue implementation in Python.
   - Identify patterns like level order traversal or sliding window.

4. **Write Code**:
   - Use clear variable names (`queue`, `front`).
   - Handle edge cases (e.g., empty queue).

5. **Test**:
   - Test with provided examples.
   - Add edge cases like empty input or large sequences.

---

## Common Techniques:
1. **Sliding Window**:
   - Use a queue to maintain a window of elements.
   - Example: Maximum in a sliding window.

2. **Level Order Traversal**:
   - Use a queue for breadth-first search in trees.
   - Example: Traverse a binary tree level by level.

3. **Monotonic Queue**:
   - Maintain a queue with increasing or decreasing order.
   - Example: Find the maximum in a sliding window.

4. **Circular Queue**:
   - Use a fixed-size array for a circular queue implementation.
   - Example: Design a bounded blocking queue.

5. **Double-Ended Queue (Deque)**:
   - Use `collections.deque` for operations at both ends.
   - Example: Sliding window problems or palindrome checking.

---

## Example LeetCode Questions:
1. **Implement Queue Using Stacks**:
   - Use two stacks to simulate queue behavior.

2. **Sliding Window Maximum**:
   - Use a monotonic deque to find the max in each window.

3. **Binary Tree Level Order Traversal**:
   - Use a queue for breadth-first traversal of the tree.

4. **Design Circular Queue**:
   - Implement a circular queue with fixed capacity.

5. **Time-Based Key-Value Store**:
   - Use a queue to store timestamps and perform range queries.

---

## Tips:
- **Initialization**: Use `deque` for efficient queue operations.
- **Edge Cases**: Consider empty queues, single element, or full queues (circular).
- **Time Complexity**: Use queue operations efficiently to avoid `O(n)` traversals.
- **Debugging**: Trace enqueue and dequeue operations step by step.

---

Practice these problems to master queue-based algorithms and patterns!
