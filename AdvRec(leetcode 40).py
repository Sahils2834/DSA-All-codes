#leetcode 40
#Combination Sum II
#algorithm = sort the candidates first to group duplicates together
#use backtracking; each element can be used only once (recurse to i+1)
#skip duplicates at the same recursion level: if i > start and candidates[i] == candidates[i-1], continue
#prune: if candidates[i] > target, break (sorted array, no need to go further)
#base case: if target == 0, add current subset copy to result
#tc: O(2^n) n is the number of candidates
#sc: O(n)

class Solution:
    def backtrack(self, start, target, subset, result, candidates):
        if target == 0:
            result.append(subset[:])
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break

            subset.append(candidates[i])
            self.backtrack(i + 1, target - candidates[i], subset, result, candidates)
            subset.pop()

    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        self.backtrack(0, target, [], result, candidates)
        return result
