# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

class Solution(object):
  def maxPathSum(self, root):
      """
      :type root: TreeNode
      :rtype: int
      """
      # Initialize the global variable to track the maximum path sum
      self.max_sum = float('-inf')

      # Helper function to compute the maximum path sum for each node
      def helper(node):
          # Base case: if the node is None, return 0
          if not node:
              return 0

          # Recursively get the maximum path sum from the left and right subtrees
          left_sum = max(helper(node.left), 0)  # If the sum is negative, ignore it (use 0)
          right_sum = max(helper(node.right), 0)

          # Calculate the maximum path sum passing through the current node
          current_sum = node.val + left_sum + right_sum

          # Update the global max_sum if the current path sum is greater
          self.max_sum = max(self.max_sum, current_sum)

          # Return the maximum sum that can be obtained by including the current node
          # as part of a path (either through the left or right child)
          return node.val + max(left_sum, right_sum)

      # Start the recursive process
      helper(root)

      # Return the global maximum path sum found
      return self.max_sum
