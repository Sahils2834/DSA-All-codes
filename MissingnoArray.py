#leetcode 268.
#timecomplexity:O(n)
#spacecomplexity:O(1)

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        return (n*(n+1)//2) - sum(nums)
        
