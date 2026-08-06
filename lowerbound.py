#lowerbound-finding first element in array that is greater than or equal to target
#algorithm = use binary search to find the first element >= target
#if arr[mid] >= target, this might be the answer, record it in ans and search left (high = mid - 1)
#if arr[mid] < target, the answer must be in the right half, search right (low = mid + 1)
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
