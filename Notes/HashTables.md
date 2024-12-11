
# Hash Tables & Solving LeetCode Questions

## Basics of Hash Tables:
1. **Definition**: A data structure that maps keys to values using a hash function.
2. **Key Operations**:
   - **Insert**: Add a key-value pair. `O(1)` on average.
   - **Search**: Find value by key. `O(1)` on average.
   - **Delete**: Remove a key-value pair. `O(1)` on average.
3. **Collisions**:
   - Handled by techniques like chaining (linked lists) or open addressing (probing).

---

## Steps to Solve Hash Table Problems:
1. **Understand the Problem**:
   - Identify the need for fast lookups, counts, or uniqueness.
   - Check constraints (e.g., size of keys, collisions).

2. **Think Through Examples**:
   - Use small examples to test the logic of hash operations.

3. **Choose an Approach**:
   - Use a dictionary (hash map) in Python for simplicity.
   - Use sets for unique elements or membership checks.

4. **Write Code**:
   - Use hash functions for custom keys (if needed).
   - Handle edge cases (e.g., duplicate keys).

5. **Test**:
   - Test with provided examples.
   - Add edge cases (e.g., empty hash, large datasets).

---

## Common Techniques:
1. **Counting with Hash Map**:
   - Count frequencies of elements.
   - Example: Find the majority element in an array.

2. **Finding Duplicates**:
   - Use a set to track seen elements.
   - Example: Check if a list has duplicates.

3. **Two Sum Using Hash Map**:
   - Store seen numbers and their indices for quick lookup.
   - Example: Two Sum problem.

4. **Grouping Elements**:
   - Use a hash map to group elements by a key.
   - Example: Group anagrams by sorted string.

5. **Caching with Hash Map**:
   - Store precomputed results for reuse.
   - Example: LRU Cache implementation.

6. **Custom Hashing**:
   - Implement custom hash functions for objects.
   - Example: Hash maps with composite keys.

---

## Example LeetCode Questions:
1. **Two Sum**:
   - Use a hash map for `O(n)` time complexity.

2. **Group Anagrams**:
   - Use a hash map with sorted strings as keys.

3. **Top K Frequent Elements**:
   - Use a hash map to count frequencies and a heap for sorting.

4. **Subarray Sum Equals K**:
   - Use a hash map to store prefix sums.

5. **Longest Consecutive Sequence**:
   - Use a set for efficient lookups.

6. **Isomorphic Strings**:
   - Use two hash maps to track character mappings.

---

## Tips:
- **Initialization**: Use `dict` or `set` in Python for hash table operations.
- **Edge Cases**: Handle empty inputs, large datasets, and collisions.
- **Custom Keys**: Use tuples or immutable objects as hash keys if needed.
- **Debugging**: Print hash table contents to understand the mapping.

---

Practice hash table problems to build efficiency in lookups and data organization!
