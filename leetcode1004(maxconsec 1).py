#Leetcode 1004(max consec 1)
#algorithm = sliding window with left and right pointers
#expand right pointer: if nums[right] == 0, increment zero count
#if zero count > k, shrink window from left (if nums[left] == 0, decrement zeros), move left forward
#update max window length whenever zeros <= k
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