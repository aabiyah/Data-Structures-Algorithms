# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution:
  def combinationSum(self, candidates, target):
      result = []

      def backtrack(start, current_combination, current_sum):
          # If the current sum equals the target, add the current combination to the result
          if current_sum == target:
              result.append(list(current_combination))  # Make a copy of the combination
              return
          # If the current sum exceeds the target, no need to continue
          if current_sum > target:
              return

          # Explore the candidates from the current position onward
          for i in range(start, len(candidates)):
              current_combination.append(candidates[i])  # Add current number to the combination
              backtrack(i, current_combination, current_sum + candidates[i])  # Allow the same number again
              current_combination.pop()  # Backtrack, remove the last added number

      # Start backtracking from index 0 with an empty combination and sum 0
      backtrack(0, [], 0)

      return result