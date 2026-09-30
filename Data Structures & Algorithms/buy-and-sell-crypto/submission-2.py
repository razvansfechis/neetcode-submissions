class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_val = prices[0]
        
        for sell_day in prices:
            max_profit = max(max_profit, sell_day - min_val)
            min_val = min(min_val, sell_day)
        
        return max_profit