#leetcode 45(Jump Game 2)
#problem statement : You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. Return true if you can reach the last index, or false otherwise.
#algorithm : We use a greedy approach. We iterate through the array and keep track of the maximum index we can reach. If we can reach the last index, we return true. Otherwise, we return false.
#time complexity : O(n)
#space complexity : O(1)

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jump = 0
        left = 0
        right = 0
        while right < n-1:
            farthest = 0
            for i in range(left, right+1):
                farthest = max(farthest,i + nums[i])
            left = right + 1
            right = farthest
            jump += 1
        return jump