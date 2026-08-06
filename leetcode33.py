#leetcode 33-search in rotated sorted array
#algorithm = modified binary search; at least one half of the array is always sorted
#if left half is sorted (nums[low] <= nums[mid]), check if target is in left half, else search right
#if right half is sorted, check if target is in right half, else search left
#time complexity: O(log2(n))
#space complexity: O(1)

class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            if  nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else: 
                    high = mid - 1
            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1