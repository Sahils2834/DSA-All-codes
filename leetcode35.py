#leetcode 35-search insert position
#algorithm = binary search to find the lower bound (first element >= target)
#if element is found, it returns its index; if not, it returns the index where it should be inserted
#if target is greater than all elements, lb remains n
#time complexity: O(log2(n))
#space complexity: O(1)

class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        lb = n
        low = 0
        high = n-1
        while low <= high:
            mid =(low + high)//2
            if nums[mid]>= target:
                lb =mid
                high = mid-1
            else:
                low = mid+1
        return lb
