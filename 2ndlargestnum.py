
#algorithm = use two variables: largest and secondlargest, both initialized to -infinity
#traverse the array once; if current element > largest, update secondlargest = largest then largest = current
#elif current element > secondlargest and not equal to largest, update secondlargest = current
#this finds the 2nd largest in a single pass without sorting
#time complexity = O(n)
#space complexity = O(1)

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

