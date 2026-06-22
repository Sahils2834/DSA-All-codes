#lowerbound-finding first element in array that is greater than or equal to target
#time complexity: O(log2(n))
#space complexity: O(1)

def lowerbound(arr,target):
    low=0
    high=len(arr)-1
    ans=-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
