#leetcode 18 4sum(Brute Force)
#time complexity:O(n^4)
#space complexity:O(n^2)

class Solution(object):
    def fourSum(self, nums, target):
        result = set()
        n = len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):
                        temp=(nums[i]+nums[j]+nums[k]+nums[l])
                        if temp == target:
                            temp.sort()
                            result.add(tuple(temp))
        result=[]
        for ans in result:
            ans.append(list(ans))
        return result

    


                            
                        
