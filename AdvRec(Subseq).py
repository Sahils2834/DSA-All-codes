class Recursion:
    def solve(self, ind, subset, nums, result):
        if ind == len(nums):
            result.append(subset.copy())
            return

        subset.append(nums[ind])
        self.solve(ind + 1, subset, nums, result)

        subset.pop()
        self.solve(ind + 1, subset, nums, result)

            
