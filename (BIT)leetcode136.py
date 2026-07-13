#leetcode 136
#title->Single Number
#topic->BIT(Binary Indexed Tree)/Number theory
#difficulty->EASY
#time->O(n)
#space->O(1)
#problem statement

class Solution(object):
    def singleNumber(self, nums):
        ans = 0

        for num in nums:
            ans ^= num

        return ans