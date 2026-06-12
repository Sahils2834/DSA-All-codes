#leetcode 53.
#timecomplexity: O(n^2)
#spacecomplexity: O(1)
# this will give max sum of subarrays.(brute force solution)

class Solution(object):
    def maxSubArray(self, nums):
        maxi = float("-inf")
        total = 0
        n = len(nums)
        for i in range(0,n):
            total = 0
            for j in range(i,n):
                total=total + nums[j]
                maxi= max(maxi,total)
        return maxi