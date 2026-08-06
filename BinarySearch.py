#binary search implementation
#itterative
#algorithm = use two pointers, low and high, to represent the search space
#calculate mid = low + (high - low) // 2 to avoid overflow
#if target == arr[mid], return mid
#if target > arr[mid], discard left half (low = mid + 1)
#if target < arr[mid], discard right half (high = mid - 1)
#time complexity: O(log n)
#space complexity: O(1)

def binary(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
