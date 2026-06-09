def get_largest(nums):
    largest = nums[0]
    n = len(nums)
    for i in range(0,n):
        largest = max(largest, nums[i])
    return largest

