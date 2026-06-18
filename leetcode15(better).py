#leetcode 15 3sum(Better Approach)
#time complexity:O(n^2)
#space complexity:O(n)


def threeSum(nums):
    n=len(nums)
    result=set()
    for i in range(0,n):
        my_set = set()
        for j in range(i+1,n-1):
            target=0-(nums[i]+nums[j])
            if target in my_set:
                temp = (nums[i],nums[j],target)
                temp = sorted(temp)
                result.add(tuple(temp))
            my_set.add(nums[j])
    return list(result)
    