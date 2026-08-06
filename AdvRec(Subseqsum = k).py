#Advanced recurssion --> to find all subsequences whose sum equals target
#algorithm = use pick/not-pick recursion with a running total
#pick: add nums[ind] to subset and total, recurse to ind+1
#not pick: remove element, restore total, recurse to ind+1
#base case: if total == target, add subset copy to result (return)
#prune: if total > target, return early (no need to explore further)
#if index >= len(nums) and total != target, simply return
#Tc --> O(2^n)
#sc --> O(n)

class recurssion():
    def solve(self,ind,subset,nums,target,total):
        result = []
        if total == target:
            result.append(subset.copy())
            return
        elif total > target:
            return
        
        if ind >= len(nums):
            return 

        subset.append(nums[ind])
        sum = total + nums[ind]
        self.solve(ind+1,subset,sum)
        e = subset.pop()
        sum = sum - e
        self.solve(ind+1,subset,sum)
