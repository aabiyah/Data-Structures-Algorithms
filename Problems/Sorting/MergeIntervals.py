# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
  def merge(self, intervals):
      """
      :type intervals: List[List[int]]
      :rtype: List[List[int]]
      """
      # Step 1: Sort intervals based on the start times
      intervals.sort(key=lambda x: x[0])

      # Step 2: Initialize result list
      merged = []

      for interval in intervals:
          # If merged is empty or the current interval does not overlap with the last one, add it
          if not merged or merged[-1][1] < interval[0]:
              merged.append(interval)
          else:
              # Otherwise, merge the intervals by updating the end time
              merged[-1][1] = max(merged[-1][1], interval[1])

      return merged