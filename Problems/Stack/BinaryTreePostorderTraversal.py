# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Base case: if the tree is empty, return an empty list
        if not root:
            return []

        # Postorder traversal: Left → Right → Root
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
