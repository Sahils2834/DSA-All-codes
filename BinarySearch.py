#binary search implementation
#itterative
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
