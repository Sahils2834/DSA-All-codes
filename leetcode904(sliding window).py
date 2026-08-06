# LeetCode 904. Fruit Into Baskets
# You are given an integer array fruits of length n, where fruits[i] is the type of fruit the ith tree produces.
# You want to collect as much fruit as possible. However, the baskets constraint:
# You can only carry two types of fruit at a time.
# Given the integer array fruits, return the maximum number of fruits you can collect.
#algorithm = use sliding window with a dictionary to track fruit frequencies
#expand right window; if dictionary has > 2 types, shrink left window until valid
#update maximum window size on each valid iteration
#tc: O(n), sc: O(1)

class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        n = len(nums)

        L = 0
        maxi = 0
        mydict = {}

        for R in range(n):
            mydict[nums[R]] = mydict.get(nums[R], 0) + 1

            if len(mydict) > 2:
                mydict[nums[L]] -= 1

                if mydict[nums[L]] == 0:
                    del mydict[nums[L]]

                L += 1

            maxi = max(maxi, R - L + 1)

        return maxi