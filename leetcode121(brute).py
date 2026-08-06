#leetcode 121.
#algorithm = try every pair (i, j) where i < j; compute prices[j] - prices[i]
#track the maximum profit across all pairs
#timecomplexity: O(n^2)
#spacecomplexity: O(1)
#this will give max profit of stocks.(brute force solution)
class Solution(object):
    def maxProfit(self, prices):
        maxi = 0
        n = len(prices)

        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                maxi = max(maxi, profit)

        return maxi
        