#leetcode 78
#topic->backtracking
#time->O(2^n *n)
#space->O(2^n)
#problem statement

class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        subset = 1<<n
        result = []
        for num in range(0,subset):
            lst = []

            for i in range(0,n):
                if num & (1<<i) != 0:
                    lst.append(nums[i])
            result.append(lst)
        return result