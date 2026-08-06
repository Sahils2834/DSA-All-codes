#leetcode 216 Combination Sum 3
#algorithm = use backtracking; iterate from 'last' to 9 (digits 1-9, no repeat)
#at each step add digit i to nums, recurse with updated sum and start = i+1
#backtrack by popping the digit after recursion
#base case: if sum == n and len(nums) == k, found a valid combination, add to ans
#prune: if sum > n or len(nums) > k, stop exploring
#TCO: O(2^n)
#SCO: O(n)

class Solution:
    def solve(self, n, Sum, last, nums, k, ans):
        if Sum == n and len(nums) == k:
            ans.append(list(nums))
            return
        
        if Sum > n or len(nums) > k:
            return

        for i in range(last , 10):
            nums.append(i)
            self.solve(n, Sum + i, i + 1, nums, k, ans) 
            nums.pop()


    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        nums=[]
        self.solve(n, 0 , 1, nums, k, ans)
        return ans
