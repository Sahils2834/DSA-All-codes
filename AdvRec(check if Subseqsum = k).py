#Advanced recurssion --> to check if any subsequence whose sum equals target exists
#algorithm = use pick/not-pick recursion; return True as soon as a valid subsequence is found
#pick path: if it returns True, propagate True immediately (short-circuit)
#not-pick path: try without the current element if pick returned False
#prune: if total > target or index out of bounds, return False
#base case: if total == target, return True
#Tc --> O(2^n)
#sc --> O(n)

class recurssion():
    def solve(self,ind,subset,nums,target,total,pick):
        result = []
        if total == target:
            result.append(subset.copy())
            return True
        elif total > target:
            return False
        
        if ind >= len(nums):
            return False

        subset.append(nums[ind])
        sum = total + nums[ind]
        pick = self.solve(ind+1,subset,sum)
        if pick == True:
            return True

        subset.pop()
        sum = total
        notpick = self.solve(ind+1,subset,total)
        return notpick