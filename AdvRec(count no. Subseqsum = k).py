#Advanced recurssion --> to count number of subsequences whose sum equals target
#algorithm = use pick/not-pick recursion returning integer counts
#pick: add nums[ind] to total, recurse and get count from pick path
#not pick: keep total same, recurse and get count from not-pick path
#return pick + notpick (total valid subsequences from this point)
#base case: if total == target return 1 (found one valid subsequence)
#prune: if total > target or index out of bounds, return 0
#Tc --> O(2^n)
#sc --> O(n)

class recurssion():
    def solve(self,ind,nums,target,total):
        if total == target:
            return 1
        elif total > target:
            return 0
        
        if ind >= len(nums):
            return 0

        sum= total + nums[ind]
        pick = self.solve(ind + 1,sum)

        sum = total
        notpick= self.solve(ind + 1,sum)
        return pick + notpick
