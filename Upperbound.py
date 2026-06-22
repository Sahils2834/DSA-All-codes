#upperbound
#time complexity: O(log2(n))
#space complexity: O(1)
#in this problem we find first element greater than target

class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        lb = n
        low = 0
        high = n-1
        while low <= high:
            mid =(low + high)//2
            if nums[mid] > target:
                lb =mid
                high = mid-1
            else:
                low = mid+1
        return lb


        