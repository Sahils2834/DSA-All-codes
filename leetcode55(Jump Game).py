#leetcode 55(Jump Game)
#problem statement : You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. Return true if you can reach the last index, or false otherwise.
#algorithm : We use a greedy approach. We iterate through the array and keep track of the maximum index we can reach. If we can reach the last index, we return true. Otherwise, we return false.
#time complexity : O(n)
#space complexity : O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])
        return True