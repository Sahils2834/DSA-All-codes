#move zeros to the end code leetcode 283
#algorithm = use two pointers, i (position for next non-zero) and j (current element)
#if nums[j] is not 0, swap nums[i] and nums[j], then increment i
#time complexity O(n)
#space complexity O(1)

class Solution(object):
    def moveZeroes(self, nums):
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1