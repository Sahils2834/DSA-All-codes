#leetcode 128- Longest Consecutive Sequence(brute force solution)
#time complexity- O(n^2)
#space complexity- O(1)

class Solution(object):
    def longestConsecutive(self, nums):
        n = len(nums)
        max_count = 0
        for i in range(0,n):
            num = nums[i]
            count = 1
            while num+1 in nums:
                count += 1
                num = num+1
                max_count = max(max_count,count)
        return max_count
        
