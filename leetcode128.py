#leetcode 128- Longest Consecutive Sequence(optimal solution)
#algorithm = add all numbers to a HashSet for O(1) lookups
#for each number, only start counting if num-1 is NOT in the set (it's a sequence start)
#from the start, keep incrementing and checking if next number exists in set
#track the longest count found
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