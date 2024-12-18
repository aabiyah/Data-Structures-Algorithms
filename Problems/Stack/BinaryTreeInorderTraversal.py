# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# To perform an inorder traversal of a binary tree, we visit the nodes in the following order:
# 1. Left subtree
# 2. Root node
# 3. Right subtree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []  
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)