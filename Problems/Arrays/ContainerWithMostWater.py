# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

class Solution(object):
  def maxArea(self, height):
      # Initialize two pointers
      left = 0
      right = len(height) - 1

      # Initialize variable to store the maximum area
      max_area = 0

      # Iterate while the two pointers don't meet
      while left < right:
          # Calculate the current area
          current_area = min(height[left], height[right]) * (right - left)

          # Update the maximum area if the current area is greater
          max_area = max(max_area, current_area)

          # Move the pointer corresponding to the shorter line
          if height[left] < height[right]:
              left += 1
          else:
              right -= 1

      return max_area
