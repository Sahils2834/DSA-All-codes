#leetcode 1.
#timecomplexity:O(n)
#spacecomplexity: O(n)
#this will give the indices of two elements that add up to the target.

class Solution(object):
    def twosum(self, nums,target):
        dict = {}
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1, n):
                remain = target - nums[j]
                if remain in dict:
                    return {dict[remain],i}
                dict[nums[i]]=i
