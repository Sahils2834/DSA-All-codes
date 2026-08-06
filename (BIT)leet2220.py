#leetcode 2220 - Minimum Bit Flips to Convert Number
#algorithm = XOR start and goal to get a number where set bits represent differing positions
#then count the number of set bits (1s) in the XOR result using a loop and bit masking
#each set bit in the XOR result corresponds to one flip needed
#time complexity : O(log N)
#space complexity : O(1)

class Solution(object):
    def minBitFlips(self, start, goal):
        ans = start ^ goal
        count = 0

        for i in range(32):
            if (ans & (1 << i)) != 0:
                count += 1

        return count