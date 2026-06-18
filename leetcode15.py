#leetcode 15 3sum(Brute Force Approach)
#time complexity:O(n^3)
#space complexity:O(n^2)
def threeSum(nums):
    n=len(nums)
    result=set()
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k]==0:
                    temp = (nums[i],nums[j],nums[k])
                    temp = sorted(temp)
                    result.add(tuple(temp))
    return list(result)

