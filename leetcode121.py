#leetcode 121.
#algorithm = track the minimum price seen so far while traversing
#at each day, compute profit = current price - min_price seen so far
#update max_profit if this profit is greater
#single pass: update min_price before computing profit
#timecomplexity: O(n)
#spacecomplexity: O(1)
#this will give max profit of stocks.

class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        n = len(prices)
        min_price = float("inf")
        for i in range(0,n):
            min_price = min(min_price,prices[i])
            max_profit = max(max_profit, prices[i]- min_price)
        return max_profit
