# LeetCode 1423. Maximum Points You Can Obtain from Cards
# You are given an integer array cardPoints and an integer k.
# In one step, you can take one card from the beginning or from the end of the array.
# Return the maximum score you can obtain after taking exactly k cards.
#algorithm = compute initial sum of first k cards (left sum = LS)
#then slide the window: remove cards from the left end one by one and add cards from the right end
#at each step update maxi = max(maxi, LS + RS); the best combination of left+right picks
#tc: O(k), sc: O(1)


class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        LS = 0
        RS = 0
        n = len(nums)
        if len(nums) == k:
            return sum(nums)
        for i in range(0,k):
            LS += nums[i]
        maxi = LS
        RI = n-1
        for i in range(k-1, -1, -1):
            LS -= nums[i]
            RS += nums[RI]
            maxi = max(maxi,LS+RS)
            
            RI -= 1
        return maxi
    