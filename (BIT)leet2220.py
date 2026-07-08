#leetcode 2220 - Minimum Bit Flips to Convert Number
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