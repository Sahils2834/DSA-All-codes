#generate all subsequences using recursion (pick / not-pick pattern)
#algorithm = at each index, make two recursive calls:
#  1. pick: include nums[ind] in subset, then recurse to ind+1
#  2. not pick: skip nums[ind], recurse to ind+1 without adding
#base case: when ind == len(nums), add a copy of the current subset to result
#this explores all 2^n combinations
#time complexity = O(2^n * n)
#space complexity = O(n) recursion stack + O(2^n * n) for result storage
class Recursion:
    def solve(self, ind, subset, nums, result):
        if ind == len(nums):
            result.append(subset.copy())
            return

        subset.append(nums[ind])
        self.solve(ind + 1, subset, nums, result)

        subset.pop()
        self.solve(ind + 1, subset, nums, result)

            
