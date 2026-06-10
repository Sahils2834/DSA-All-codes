
def second(nums):
    largest = float("-inf")
    secondlargest = float("-inf")
    n = len(nums)
    for i in range(0,n):
        if nums[i] > largest:
            secondlargest = largest
            largest = nums[i]

        elif nums[i] > secondlargest and secondlargest != largest:
            secondlargest= nums[i]

    return secondlargest

