#Advanced recurssion ---> to find number of subsequnce whose sum is target
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