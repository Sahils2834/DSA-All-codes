#leetcode 485.
#timecomplexity:O(n)
#spacecomplexity:O(1)
#this will give max no. of consecutive 1s.

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_count = 0
        n = len(nums)

        for i in range(0,n):
            if nums[i] == 1:
                count +=1
            else:
                max_count = max(max_count,count)
                count = 0
        return max(max_count,count)
