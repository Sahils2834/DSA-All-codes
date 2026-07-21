#Advanced recurssion ---> to find number of subsequnce whose sum is target
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
