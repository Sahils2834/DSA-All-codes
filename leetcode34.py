#leetcode 34-find first and last position of element in sorted array
#time complexity: O(log2(n))
#space complexity: O(1)

class Solution(object):
    def searchRange(self, nums, target):

        def lowerbound(nums, target):
            n = len(nums)
            lb = n
            low, high = 0, n - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] >= target:
                    lb = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return lb

        def upperbound(nums, target):
            n = len(nums)
            ub = n
            low, high = 0, n - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] > target:
                    ub = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return ub

        lb = lowerbound(nums, target)

        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]

        ub = upperbound(nums, target)

        return [lb, ub - 1]