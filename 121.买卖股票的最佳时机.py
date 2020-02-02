#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 : return 0
        
        buy_price = prices[0]
        profit = 0
        
        for i in range(len(prices)):
            buy_price = min(buy_price, prices[i])
            profit = max(profit,  prices[i] - buy_price)
        return profit
# @lc code=end
