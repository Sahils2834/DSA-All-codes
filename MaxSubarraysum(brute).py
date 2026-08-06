#leetcode 53.
#algorithm = brute force: try every possible subarray using two nested loops
#outer loop picks the starting index i, inner loop extends to j
#keep a running total and update maxi for every subarray [i..j]
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