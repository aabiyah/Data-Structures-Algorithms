
# Trees & Solving LeetCode Questions

## Basics of Trees:
1. **Definition**: A hierarchical data structure with nodes connected by edges.
2. **Key Properties**:
   - Root: The topmost node.
   - Parent/Child: Relationships between nodes.
   - Leaf: A node with no children.
   - Height: Longest path from root to leaf.
3. **Types of Trees**:
   - Binary Tree: Each node has at most two children.
   - Binary Search Tree (BST): Left child < parent < right child.
   - Balanced Tree: Height is minimized (e.g., AVL, Red-Black Tree).
   - Complete Tree: All levels filled except possibly the last.
   - Full Tree: Every node has 0 or 2 children.
   - Trie: A tree for storing strings.

---

## Steps to Solve Tree Problems:
1. **Understand the Problem**:
   - Identify the tree structure (binary tree, BST, etc.).
   - Check constraints (e.g., height, number of nodes).

2. **Think Through Examples**:
   - Use small trees to simulate operations manually.

3. **Choose an Approach**:
   - Recursive: Simplify problem by solving subproblems.
   - Iterative: Use stacks/queues for traversal.
   - Use properties of BSTs for optimized solutions.

4. **Write Code**:
   - Use helper functions for recursive solutions.
   - Handle edge cases (e.g., empty tree, single node).

5. **Test**:
   - Test with provided examples.
   - Add edge cases (e.g., skewed trees, null nodes).

---

## Common Techniques:
1. **Traversal**:
   - Inorder: Left -> Root -> Right (used for sorted order in BSTs).
   - Preorder: Root -> Left -> Right.
   - Postorder: Left -> Right -> Root.
   - Level Order: Use a queue for breadth-first traversal.

2. **Recursive Solutions**:
   - Base case for null nodes.
   - Solve left and right subtrees recursively.

3. **DFS and BFS**:
   - DFS: Use recursion or a stack for depth-first search.
   - BFS: Use a queue for breadth-first search.

4. **Binary Search Tree Properties**:
   - Efficiently find min/max, search, and insert/delete.

5. **Dynamic Programming on Trees**:
   - Use postorder traversal for subtree calculations.
   - Example: Maximum path sum.

6. **LCA (Lowest Common Ancestor)**:
   - Use recursion or iterative traversal for finding LCA.

---

## Example LeetCode Questions:
1. **Binary Tree Inorder Traversal**:
   - Use recursion or a stack for iterative traversal.

2. **Maximum Depth of Binary Tree**:
   - Use DFS or BFS to calculate depth.

3. **Path Sum**:
   - Use DFS to track the sum of nodes along a path.

4. **Validate Binary Search Tree**:
   - Use inorder traversal or recursion with bounds.

5. **Lowest Common Ancestor of BST**:
   - Use BST properties to optimize.

6. **Serialize and Deserialize Binary Tree**:
   - Use BFS for level order serialization.

7. **Construct Binary Tree from Traversals**:
   - Use preorder and inorder/postorder arrays.

---

## Tips:
- **Initialization**: Start with root node and traversal methods.
- **Edge Cases**: Handle empty trees, single-node trees, and skewed trees.
- **Debugging**: Use print statements to visualize tree structure.
- **Time Complexity**: Aim for `O(n)` traversal solutions.
- **Space Complexity**: Consider recursive stack space for DFS.

---

Practice tree problems to master hierarchical data structure operations and traversal techniques!
