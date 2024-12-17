class Solution:
  def intToRoman(self, num: int) -> str:
      # Define the Roman numeral symbols and their corresponding values
      roman_map = [
          ("M", 1000), 
          ("CM", 900), 
          ("D", 500), 
          ("CD", 400), 
          ("C", 100), 
          ("XC", 90), 
          ("L", 50), 
          ("XL", 40), 
          ("X", 10), 
          ("IX", 9), 
          ("V", 5), 
          ("IV", 4), 
          ("I", 1)
      ]

      # Initialize the result as an empty string
      result = ""

      # Iterate through the list of Roman numeral symbols
      for symbol, value in roman_map:
          # While the current number is greater than or equal to the Roman value
          while num >= value:
              result += symbol  # Append the Roman symbol to the result
              num -= value  # Subtract the value from the number

      return result
