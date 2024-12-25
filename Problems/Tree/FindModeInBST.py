# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder_traversal(node):
            if node is None:
                return

            inorder_traversal(node.left)  # Traverse the left subtree

            # Process the current node
            if node.val == self.current_val:
                self.current_count += 1
            else:
                self.current_val = node.val
                self.current_count = 1

            # Check if we found a new mode or need to update the modes
            if self.current_count > self.max_count:
                self.max_count = self.current_count
                self.modes = [node.val]  # Found a new mode, reset the list
            elif self.current_count == self.max_count:
                self.modes.append(node.val)  # Current value is part of the modes

            inorder_traversal(node.right)  # Traverse the right subtree

        # Initialize variables
        self.current_val = None  # To store the current value being processed
        self.current_count = 0  # To store the frequency of the current value
        self.max_count = 0  # To store the maximum frequency encountered
        self.modes = []  # To store the modes

        inorder_traversal(root)  # Start the inorder traversal

        return self.modes  # Return the modes found