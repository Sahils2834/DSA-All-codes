#next greater element2 
#algorithm = we need an empty stack and ans=array of size n initialized with -1 
#also we need to take duplicate of our array by taking nums[i%n]
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