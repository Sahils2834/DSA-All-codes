#Advanced recurssion ---> to find number of subsequnce whose sum is target
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
