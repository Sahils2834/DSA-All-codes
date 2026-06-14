#leetcode 128- Longest Consecutive Sequence(optimal solution)
#time complexity- O(n)
#space complexity- O(n)

class Solution(object):
    def longestConsecutive(self, nums):
        n = len(nums)
        my_set = set()
        longest = 0

        for i in range(n):
            my_set.add(nums[i])

        for num in my_set:
            if num - 1 not in my_set:
                x = num
                count = 1

                while x + 1 in my_set:
                    count += 1
                    x += 1

                longest = max(longest, count)

        return longest