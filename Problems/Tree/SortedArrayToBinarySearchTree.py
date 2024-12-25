# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # Helper function to construct the BST
        def convertListToBST(left, right):
            if left > right:
                return None

            mid = (left + right) // 2  # Find the middle element
            root = TreeNode(nums[mid])  # Create the root node with the middle element
            print("Creating node with value: {}".format(root.val))  # Debugging line to see node creation

            # Recursively construct the left and right subtrees
            root.left = convertListToBST(left, mid - 1)
            root.right = convertListToBST(mid + 1, right)

            return root

        # Start the recursion with the full range of the array
        return convertListToBST(0, len(nums) - 1)
