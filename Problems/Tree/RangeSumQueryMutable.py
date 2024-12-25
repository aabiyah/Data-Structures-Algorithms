# Given an integer array nums, handle multiple queries of the following types:

# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be val.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

class SegmentTree:
  def __init__(self, nums):
      self.n = len(nums)
      self.tree = [0] * (2 * self.n)
      # Build the segment tree
      for i in range(self.n):
          self.tree[self.n + i] = nums[i]
      for i in range(self.n - 1, 0, -1):
          self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

  def update(self, index, val):
      # Update the value at index
      index += self.n  # Shift index to the leaf node position
      self.tree[index] = val
      # Recalculate the segment tree
      index //= 2
      while index >= 1:
          self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]
          index //= 2

  def query(self, left, right):
      # Query the sum in the range [left, right]
      left += self.n  # Shift left to the leaf node position
      right += self.n  # Shift right to the leaf node position
      sum_result = 0
      while left <= right:
          if left % 2 == 1:
              sum_result += self.tree[left]
              left += 1
          if right % 2 == 0:
              sum_result += self.tree[right]
              right -= 1
          left //= 2
          right //= 2
      return sum_result

class NumArray:
  def __init__(self, nums):
      self.segment_tree = SegmentTree(nums)

  def update(self, index, val):
      self.segment_tree.update(index, val)

  def sumRange(self, left, right):
      return self.segment_tree.query(left, right)