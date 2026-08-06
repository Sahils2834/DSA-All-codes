#rotate the array for k elements
#algorithm = use reverse helper function to reverse parts of the array
#k = k % n; reverse last k elements, reverse first n-k elements, reverse whole array
#space complexity O(1)
#time complexity O(n)

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        def rev(left,right):
            while left < right:
                nums[left],nums[right] = nums[right],nums[left]
                left +=1
                right -=1

        rev(n-k,n-1)
        rev(0,n-k-1)
        rev(0,n-1)        
        