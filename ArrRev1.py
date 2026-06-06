class Solution:
    def func(self, nums, left, right):
        if left >= right:
            return

        nums[left], nums[right] = nums[right], nums[left]
        self.func(nums, left + 1, right - 1)

    def reverseArray(self, nums, l, r):
        self.func(nums, l, r)
        return nums
