#bit subsequence 
#time complexity : O(2^n *n)
#space complexity : O(2^n)
#problem statement 

def solve(ind,subset,nums,result):
    if ind >=len(nums):
        result.append(subset.copy())
        return

    subset.append(nums[ind])
    solve(ind+1,subset)
    subset.pop()
    solve(ind+1,subset)

