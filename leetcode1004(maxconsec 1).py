#Leetcode 1004(max consec 1)
#algorithm = we will use the concept of sliding window
#time complexity = O(n)
#space complexity = O(n)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        zeros = 0
        maxi = 0
        n = len(nums)

        while right < n:
            if nums[right] == 0:
                zeros += 1

            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            if zeros <= k:
                maxi = max(maxi, right - left + 1)

            right += 1

        return maxi