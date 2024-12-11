
# Stacks & Solving LeetCode Questions

## Basics of Stacks:
1. **Definition**: A linear data structure following the **LIFO** (Last In, First Out) principle.
2. **Key Operations**:
   - **Push**: Add an element to the top of the stack. `O(1)`
   - **Pop**: Remove the top element. `O(1)`
   - **Peek/Top**: Access the top element without removing it. `O(1)`
   - **Is Empty**: Check if the stack is empty. `O(1)`

---

## Steps to Solve Stack Problems:
1. **Understand the Problem**:
   - Identify operations needed (push, pop, etc.).
   - Check constraints (e.g., stack size, input format).

2. **Think Through Examples**:
   - Use small examples to simulate stack operations manually.

3. **Choose an Approach**:
   - Use a list or `collections.deque` for stack implementation in Python.
   - Identify patterns like balanced parentheses or reversing sequences.

4. **Write Code**:
   - Use clear variable names (`stack`, `top`).
   - Handle edge cases (e.g., empty stack).

5. **Test**:
   - Test with provided examples.
   - Add edge cases like empty input or long sequences.

---

## Common Techniques:
1. **Balancing Problems**:
   - Use a stack to match pairs (e.g., parentheses, brackets).
   - Example: Check if parentheses are valid.

2. **Monotonic Stack**:
   - Maintain a stack with increasing or decreasing order.
   - Example: Find the next greater element.

3. **Reverse Using Stack**:
   - Push elements onto the stack and pop them in reverse order.
   - Example: Reverse a string or linked list.

4. **DFS/Backtracking**:
   - Use stacks for iterative depth-first search.
   - Example: Solve maze problems.

5. **Simulate Recursion**:
   - Use a stack to simulate recursive function calls.
   - Example: Evaluate postfix expressions.

---

## Example LeetCode Questions:
1. **Valid Parentheses**:
   - Use a stack to match opening and closing brackets.

2. **Min Stack**:
   - Use an auxiliary stack to track the minimum value.

3. **Daily Temperatures**:
   - Use a monotonic stack to find the next warmer day.

4. **Next Greater Element**:
   - Traverse array with a monotonic stack for efficient lookup.

5. **Evaluate Reverse Polish Notation**:
   - Use a stack to evaluate expressions in postfix notation.

---

## Tips:
- **Initialization**: Always initialize the stack before use.
- **Edge Cases**: Think about empty stack, single element, and large inputs.
- **Time Complexity**: Aim for `O(n)` solutions by using stacks efficiently.
- **Debugging**: Visualize stack operations step by step.

---

Practice these problems to master stack-based algorithms and patterns!
