# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

class Solution:
  def maxSlidingWindow(self, nums, k):
      # Deque to store indices of elements in the sliding window
      deq = deque()
      result = []

      for i in range(len(nums)):
          # Remove indices of elements not in the current window
          if deq and deq[0] < i - k + 1:
              deq.popleft()

          # Remove elements that are smaller than the current element
          while deq and nums[deq[-1]] < nums[i]:
              deq.pop()

          # Add the current element's index to the deque
          deq.append(i)

          # Add the current max to the result list once we have processed at least k elements
          if i >= k - 1:
              result.append(nums[deq[0]])

      return result