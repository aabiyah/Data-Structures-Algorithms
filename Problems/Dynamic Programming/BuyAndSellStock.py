# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
  def maxProfit(self, prices):
      """
      :type prices: List[int]
      :rtype: int
      """
      # Initialize the minimum price to a very large value and max profit to 0
      min_price = float('inf')
      max_profit = 0

      # Iterate through the prices array
      for price in prices:
          # Update the minimum price encountered so far
          if price < min_price:
              min_price = price
          # Calculate the profit if we sell at the current price
          profit = price - min_price
          # Update the maximum profit if we find a higher profit
          max_profit = max(max_profit, profit)

      return max_profit