# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

class Solution:
  def letterCombinations(self, digitsLetter Combinations of a Phone Number):
      if not digits:
          return []

      # Mapping from digit to letters
      digit_to_letters = {
          '2': ['a', 'b', 'c'],
          '3': ['d', 'e', 'f'],
          '4': ['g', 'h', 'i'],
          '5': ['j', 'k', 'l'],
          '6': ['m', 'n', 'o'],
          '7': ['p', 'q', 'r', 's'],
          '8': ['t', 'u', 'v'],
          '9': ['w', 'x', 'y', 'z']
      }

      # Result list to store all the combinations
      result = []

      # Helper function to perform backtracking
      def backtrack(index, current_combination):
          # If the current combination is complete, add it to the result
          if index == len(digits):
              result.append("".join(current_combination))
              return

          # Get the letters for the current digit
          current_digit = digits[index]
          letters = digit_to_letters[current_digit]

          # Try each letter and recurse for the next digit
          for letter in letters:
              current_combination.append(letter)  # Choose the letter
              backtrack(index + 1, current_combination)  # Recurse
              current_combination.pop()  # Un-choose the letter (backtrack)

      # Start backtracking from the first digit
      backtrack(0, [])
      return result
