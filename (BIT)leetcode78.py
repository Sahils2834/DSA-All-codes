#leetcode 78
#topic->backtracking
#algorithm = there are 2^n possible subsets for n elements
#iterate from 0 to 2^n - 1; each number represents a bitmask
#for each number, check which bits are set using (num & (1<<i))
#if bit i is set, include nums[i] in the current subset
#each unique bitmask generates a unique subset
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