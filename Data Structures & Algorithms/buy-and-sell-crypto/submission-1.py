class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_dif = 0

        min_val = 101
        max_val = -1

        for price in prices:
            if price > max_val:
                max_val = price

            if price < min_val:
                min_val = price
                max_val = price

            if max_val != min_val:
                max_dif = max(max_dif,  max_val - min_val)

        return max_dif