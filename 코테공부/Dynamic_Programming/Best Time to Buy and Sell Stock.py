#################################################################
#121. Best Time to Buy and Sell Stock                           #
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ #
#################################################################


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, ans = float('inf'), 0
        for p in prices:
            buy, ans = min(buy, p), max(ans, p-buy)
        return ans