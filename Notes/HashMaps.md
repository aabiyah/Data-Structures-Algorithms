
# Hash Maps & Solving LeetCode Questions

## Basics of Hash Maps:
1. **Definition**: A data structure that maps keys to values using a hash function.
2. **Key Operations**:
   - **Insert**: Add a key-value pair. `O(1)` on average.
   - **Search**: Find value by key. `O(1)` on average.
   - **Delete**: Remove a key-value pair. `O(1)` on average.
3. **Collisions**:
   - Handled by chaining (linked lists) or open addressing (probing).
4. **Applications**:
   - Fast lookups, frequency counting, caching, and grouping.

---

## Steps to Solve Hash Map Problems:
1. **Understand the Problem**:
   - Identify the need for fast lookups, counts, or uniqueness.
   - Check constraints (e.g., size of keys, collisions).

2. **Think Through Examples**:
   - Use small examples to test logic with hash operations.

3. **Choose an Approach**:
   - Use `dict` in Python for hash map implementation.
   - Use sets for uniqueness checks or membership tests.

4. **Write Code**:
   - Leverage hash map methods (`get`, `setdefault`).
   - Handle edge cases (e.g., duplicate keys, empty hash map).

5. **Test**:
   - Test with provided examples.
   - Add edge cases like empty hash maps or large inputs.

---

## Common Techniques:
1. **Counting with Hash Map**:
   - Count frequencies of elements or occurrences.
   - Example: Find the majority element in an array.

2. **Finding Duplicates**:
   - Use a set to track seen elements.
   - Example: Detect duplicates in an array.

3. **Two Sum Using Hash Map**:
   - Store numbers and their indices for quick lookups.
   - Example: Find two indices such that their sum equals a target.

4. **Grouping Elements**:
   - Use a hash map to group elements by a key.
   - Example: Group anagrams by sorted strings.

5. **Prefix Sums with Hash Map**:
   - Store cumulative sums to solve subarray problems efficiently.
   - Example: Subarray Sum Equals K.

6. **Custom Hashing**:
   - Use tuples or immutable objects for composite keys.
   - Example: Track pairs or combinations of elements.

---

## Example LeetCode Questions:
1. **Two Sum**:
   - Use a hash map to store indices for `O(n)` time complexity.

2. **Group Anagrams**:
   - Use a hash map with sorted strings as keys.

3. **Top K Frequent Elements**:
   - Use a hash map for counting and a heap for sorting.

4. **Longest Substring Without Repeating Characters**:
   - Use a hash map to store the last seen index of characters.

5. **Subarray Sum Equals K**:
   - Use a hash map to store prefix sums for efficient lookups.

6. **Isomorphic Strings**:
   - Use two hash maps to track character mappings.

7. **Word Pattern**:
   - Use a hash map to map pattern characters to words.

---

## Tips:
- **Initialization**: Use `dict` or `collections.defaultdict` in Python for hash map operations.
- **Edge Cases**: Handle empty inputs, duplicate keys, and large datasets.
- **Custom Keys**: Use tuples or immutable objects for complex keys.
- **Time Complexity**: Optimize for `O(1)` operations where possible.
- **Debugging**: Print hash map contents to understand key-value mappings.

---

Master hash map problems to excel in fast lookups and grouping-related challenges!
