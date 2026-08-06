#Next Greater Element

#Algorithm:
#traverse the array from right to left using a monotonic stack
#for each element, pop from the stack while the stack top is <= current element (not useful as next greater)
#if stack is not empty after popping, top is the next greater element for current index
#else next greater is -1 (no greater element to the right)
#push current element to stack before moving to the next index
#result is built right to left then returned
#time complexity = O(n)
#space complexity = O(n)
#Example:
#Input: 4,5,2,10
#Output: 5,10,10,-1


def nextGreaterElement(nums):
    stack = []
    result = []
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if len(stack) != 0:
            result[i] = stack[-1]
        stack.append(nums[i])
    return result