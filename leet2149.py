# pyrefly: ignore [missing-import]
#leetcode 2149- Rearrange Array Elements by Sign(Optimal solution)
# Time complexity- O(n)
# Space complexity- O(n)

class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        result = [0] * n
        pos_ind = 0
        neg_ind = 1
        for i in range(0,n):
            if nums[i] >= 0:
                result[pos_ind] = nums[i]
                pos_ind +=2
            else: 
                result[neg_ind] = nums[i]
                neg_ind +=2
        return result