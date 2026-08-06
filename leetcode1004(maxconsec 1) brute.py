#Leetcode 1004(max consec 1)
#algorithm (brute) = use two nested loops; fix start i, extend j counting zeros
#if zeros exceed k, break inner loop; otherwise track max window size
#algorithm (optimal) = use sliding window with left and right pointers
#expand right: count zeros; if zeros > k shrink from left (if left was 0, decrement zeros)
#update max window size whenever zeros <= k
#time complexity = O(n)
#space complexity = O(n)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi = 0
        n = len(nums)

        for i in range(n):
            zeros = 0

            for j in range(i, n):
                if nums[j] == 0:
                    zeros += 1

                if zeros > k:
                    break

                maxi = max(maxi, j - i + 1)

        return maxi



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

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            if zeros <= k:
                maxi = max(maxi, right - left + 1)

            right += 1

        return maxi

