# Given the root of a binary tree, flatten the tree into a "linked list":
# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.

class Solution(object):
  def flatten(self, root):
      """
      :type root: TreeNode
      :rtype: None Do not return anything, modify root in-place instead.
      """
      current = root
      while current:
          if current.left:
              # Find the rightmost node of the left subtree
              rightmost = current.left
              while rightmost.right:
                  rightmost = rightmost.right

              # Reconnect right subtree to the rightmost node
              rightmost.right = current.right

              # Move left subtree to the right and set left to None
              current.right = current.left
              current.left = None

          # Move to the next node (right subtree)
          current = current.right