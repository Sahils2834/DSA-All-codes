def linear(nums,k):
    n =len(nums)
    for i in range (0,n):
        if nums[i]== k:
            return i
    return -1
