#leetcode 216 Combination Sum 3
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
