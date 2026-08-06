#next greater element2 
#algorithm = use a monotonic stack and simulate a circular array by traversing twice (2*n)
#use modulo operator (i % n) to access elements circularly
#pop stack while top <= current element
#only update the answer array during the first n iterations (i < n)
#push the current element to the stack
#time complexity = O(n)
#space complexity = O(n)


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        stack = []
        for i in range(2*n-1, -1, -1):
            while len(stack) !=0 and stack[-1] <= nums[i%n]:
                stack.pop()
            if i < n:
                if len(stack) != 0:
                    ans[i] = stack[-1]
            stack.append(nums[i%n])
        return ans