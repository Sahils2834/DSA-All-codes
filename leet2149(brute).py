#leetcode 2149- Rearrange Array Elements by Sign(brute-force)
# You are given a 0-indexed integer array nums of even length 
#Time complexity- O(n)
#Space complexity- O(n)


class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        pos = []
        neg = []
        for i in range(0,n):
            if nums[i] >= 0:
                pos.append(nums[i])
            else: 
                neg.append(nums[i])

        for i in range(0,len(pos)):
            nums[2 * i] = pos[i]
            nums[(2 * i) + 1] = neg[i]
        return nums