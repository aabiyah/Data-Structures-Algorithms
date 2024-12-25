# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(t1, t2):
            # Base cases
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            # Check the current nodes' values and recursively check the subtrees
            return (t1.val == t2.val) and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        # If the tree is empty, it's symmetric
        if not root:
            return True

        # Start comparing the left and right subtrees of the root
        return isMirror(root.left, root.right)