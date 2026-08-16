#leetcode 70 : Climbing Stairs
#input: n = 2
#output: 2
#algorithm :
#1. Use dynamic programming to find the number of ways to climb the stairs
#2. If n == 1, return 1
#3. If n == 2, return 2
#4. For n > 2, return dp[n-1] + dp[n-2]
#time complexity: O(n)
#space complexity: O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one = 1
        two = 2

        for i in range(3, n + 1):
            temp = one + two
            one = two
            two = temp

        return two

    