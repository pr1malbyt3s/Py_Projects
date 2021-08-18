# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Set the initial profit to zero:
        max_profit = 0
        # set the initial low price to the first element in prices:
        low_price = prices[0]
        # Iterate through the prices list, starting at the second element until the end:
        for i in range(1, len(prices)):
            # Update the low price to the minimum of the current low price and the current prices element:
            low_price = min(low_price, prices[i])
            # Update the profit to the maximum of the current max profit and the difference between the low price and current prices element:
            max_profit = max(max_profit, prices[i] - low_price)
        return max_profit
