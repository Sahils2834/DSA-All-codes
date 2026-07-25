#Subset Sum Problem (Count Number of Subsets that sum up to a given target)

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