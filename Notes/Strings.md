
# Strings & Solving LeetCode Questions

## Basics of Strings:
1. **Definition**: A sequence of characters stored as a single entity.
2. **Indexing**: Access characters using `string[index]`. Zero-based indexing is common.
3. **Key Operations**:
   - Access: `O(1)`
   - Concatenation: `O(n)` (creates a new string)
   - Substring: `O(n)` (depends on implementation)

---

## Steps to Solve String Problems:
1. **Understand the Problem**:
   - Identify inputs/outputs (e.g., string manipulations, pattern matching).
   - Check constraints (e.g., case sensitivity, allowed characters).

2. **Think Through Examples**:
   - Use small strings to identify patterns.
   - Manually compute expected outputs.

3. **Choose an Approach**:
   - **Brute Force**: Check all possibilities (helpful for small inputs).
   - **Optimize**: Use hash maps, two pointers, sliding window, etc.

4. **Write Code**:
   - Use built-in string methods for simplicity.
   - Handle edge cases (e.g., empty strings, single character).

5. **Test**:
   - Test with provided examples.
   - Add edge cases (e.g., spaces, special characters, duplicates).

---

## Common Techniques:
1. **Two Pointers**:
   - Use for problems like reversing or comparing substrings.
   - Example: Check if a string is a palindrome.

2. **Sliding Window**:
   - Use for substring problems (fixed/variable size).
   - Example: Longest substring without repeating characters.

3. **Hash Map**:
   - Store character counts or indices for quick lookups.
   - Example: Find the first non-repeating character.

4. **String Manipulation**:
   - Use slicing, concatenation, and join methods.
   - Example: Reverse words in a string.

5. **Pattern Matching**:
   - Use algorithms like KMP or Rabin-Karp for efficient searches.
   - Example: Check if a string contains a pattern.

6. **Dynamic Programming**:
   - Use for problems involving sequences or transformations.
   - Example: Longest Palindromic Substring.

---

## Example LeetCode Questions:
1. **Valid Anagram**:
   - Approach: Sort strings or use a frequency counter.

2. **Longest Substring Without Repeating Characters**:
   - Use a sliding window with a hash set.

3. **Longest Palindromic Substring**:
   - Expand around centers or use dynamic programming.

4. **Group Anagrams**:
   - Use sorted strings as keys in a hash map.

5. **Word Search**:
   - Use backtracking for 2D board traversal.

---

## Tips:
- **Case Sensitivity**: Convert to lowercase/uppercase if needed.
- **Whitespace**: Handle leading/trailing spaces carefully.
- **Time Complexity**: Avoid unnecessary operations (e.g., repeated slicing).
- **Edge Cases**: Think about empty strings, special characters, single character strings, etc.

---

Keep practicing to improve your problem-solving skills with strings!
