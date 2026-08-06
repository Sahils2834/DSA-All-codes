#leetcode 39
#Combination Sum
#algorithm = use backtracking; same element can be used multiple times
#pick: include candidates[index], recurse at SAME index (allowing reuse), add to total
#not pick: skip current, recurse to index+1
#base case: if total == target, add subset copy to result
#prune: if total > target or index >= len, return
#tc: O(2^t) t is the target 
#sc: O(t)

class Solution(object):
    def solve(self,index,subset,nums,target,total,result):
        if total == target:
            result.append(subset.copy())
            return
        elif total > target:
            return

        if index >= len(nums):
            return
        subset.append(nums[index])
        self.solve(index, subset, nums, target, total + nums[index], result)

        subset.pop()
        self.solve(index + 1, subset, nums, target, total, result)



    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(0, [], candidates, target, 0, result)
        return result
        