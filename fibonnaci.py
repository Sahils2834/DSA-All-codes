class Solution(object):
    def fib(self, n):
        return self.func(n)

    def func(self, nums):
        if nums == 0 or nums == 1:
            return nums

        return self.func(nums - 1) + self.func(nums - 2)