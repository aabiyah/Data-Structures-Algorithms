# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

class Solution:
  def combinationSum2(self, candidates, target):
      result = []

      # First, we sort the candidates to help us avoid duplicates
      candidates.sort()

      def backtrack(start, current_combination, current_sum):
          # If the current sum equals the target, add the combination to the result
          if current_sum == target:
              result.append(list(current_combination))
              return
          # If the current sum exceeds the target, no need to continue
          if current_sum > target:
              return

          # Explore the candidates from the current position onward
          for i in range(start, len(candidates)):
              # Skip duplicates
              if i > start and candidates[i] == candidates[i - 1]:
                  continue

              # Add the current candidate to the combination
              current_combination.append(candidates[i])

              # Recursively try the next candidates, starting from the next index
              backtrack(i + 1, current_combination, current_sum + candidates[i])

              # Backtrack, remove the last added number
              current_combination.pop()

      # Start the backtracking with an empty combination and sum of 0
      backtrack(0, [], 0)

      return result