#Leetcode 735
#algorithm = take a stack and traverse the array
#if stack is empty or the current element is positive or the stack top is negative then push the element
#else if the stack top is positive and the current element is negative then check the absolute value
#if the absolute value of the current element is greater than the stack top then pop the stack
#else if the absolute value of the current element is less than the stack top then do nothing
#else if the absolute value of the current element is equal to the stack top then pop the stack
#time complexity = O(n)
#space complexity = O(n)


class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        for i in range(0,n):
            if nums[i] > 0:
                stack.append(nums[i])
            else:
                while len(stack) != 0 and stack[-1] > 0 and stack[-1] < abs(nums[i]):
                    stack.pop()
                if len(stack) != 0 and stack[-1] == abs(nums[i]):
                    stack.pop()
                elif len(stack) == 0 or stack[-1] < 0:
                    stack.append(nums[i]) 
        return stack
