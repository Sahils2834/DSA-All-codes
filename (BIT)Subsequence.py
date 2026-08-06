#bit subsequence 
#algorithm = at each index we have two choices: pick the element or not pick it
#if we pick it, add to current subset and recurse to next index
#if we don't pick, simply recurse to next index without adding
#when index reaches end of array, add the current subset copy to result
#this generates all 2^n possible subsequences
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

