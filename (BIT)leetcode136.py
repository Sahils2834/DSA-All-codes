#leetcode 136
#title->Single Number
#topic->BIT(Binary Indexed Tree)/Number theory
#difficulty->EASY
#algorithm = XOR all numbers together; any number XORed with itself becomes 0
#since all numbers appear twice except one, all pairs cancel out leaving only the single number
#time->O(n)
#space->O(1)
#problem statement

class Solution(object):
    def singleNumber(self, nums):
        ans = 0

        for num in nums:
            ans ^= num

        return ans