# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []

        # A memoization cache to store results for subproblems
        def generate_tree_range(start, end):
            # If start > end, return a list with None (empty tree)
            if start > end:
                return [None]

            result = []
            # Try each number between start and end as the root
            for root_val in range(start, end + 1):
                # Generate all possible left and right subtrees
                left_trees = generate_tree_range(start, root_val - 1)
                right_trees = generate_tree_range(root_val + 1, end)

                # Combine the left and right subtrees with the root
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        result.append(root)

            return result

        # Generate all trees for values 1 to n
        return generate_tree_range(1, n)
