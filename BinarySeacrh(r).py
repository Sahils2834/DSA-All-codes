#binary search-recursive
#time complexity: O(log2(n))
#space complexity: O(1)

def binary_r(arr,target,low,high):
    if low>high:
        return -1
    mid=low+(high-low)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binary_r(arr,target,mid+1,high)
    else:
        return binary_r(arr,target,low,mid-1)

print(binary_r([1,2,3,4,5,6,7,8,9,10],10,0,9))
