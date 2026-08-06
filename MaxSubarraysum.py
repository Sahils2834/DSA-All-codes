# pyrefly: ignore [missing-import]
# leetcode 53.
# algorithm = Kadane's algorithm: maintain a running total
# add each element to total; update maxi if total > maxi
# if total drops below 0, reset it to 0 (a negative prefix only hurts future subarrays)
# this greedily keeps the best subarray ending at each position
# timecomplexity: O(n)
# spacecomplexity: O(1)
# this will give max sum of subarrays.(kadanes algo)
class Solution(object):
    def maxSubArray(self, nums):
        maxi = float("-inf")
        total = 0
        n = len(nums)
        for i in range(0,n):
            total = total + nums[i]
            maxi = max(maxi,total)
            if(total<0):
                total=0
        return maxi