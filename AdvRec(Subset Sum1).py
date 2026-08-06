#Subset Sum Problem (Count Number of Subsets that sum up to a given target)
#algorithm = use pick/not-pick recursion to generate all subsets
#at each index, either include the element in the subset or skip it
#when all elements are processed (index >= len), record the sum of the current subset
#sort the result at the end as required by the problem
#TCO - 3^n
#TCO - O(n * Sum)

class Solution:
    def solve(self, nums, index, subset, result):
        # Base case: processed all elements
        if index >= len(nums):
            result.append(sum(subset))  # Calculate sum of current subset
            return
        
        # Choice 1: Include current element
        subset.append(nums[index])
        self.solve(nums, index + 1, subset, result)
        
        # Backtrack: Remove current element  
        subset.pop()
        
        # Choice 2: Exclude current element
        self.solve(nums, index + 1, subset, result)

    def subsetSums(self, arr):
        result = []
        self.solve(arr, 0, [], result)
        result.sort()  # Sort as required by problem
        return result