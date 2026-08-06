#leetcode 151 
#Reverse Words in a String
#(Note: code actually solves Find Minimum in Rotated Sorted Array - LC 153)
#algorithm = use binary search; if right half is sorted (nums[mid] <= nums[high])
#the minimum is in the left half or at mid; update mini = min(mini, nums[mid]) and go left
#else the left half is sorted, minimum must be in the right half; update mini = min(mini, nums[low]) and go right
#space O(1)
#time O(Log (N))

class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        low = 0
        high = n-1
        mini = float("inf")
        while low <= high:
            mid = (low + high)//2
            if nums[mid] <= nums[high]:
                mini = min(mini,nums[mid])
                high = mid -1
            else:
                mini = min(mini,nums[low]) 
                low = mid + 1
        return mini