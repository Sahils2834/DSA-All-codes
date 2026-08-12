#leetcode 14 : Longest Common Prefix
#Algorithm
#1. Create a variable to store the longest common prefix.
#2. Iterate through the array of strings from left to right.
#3. For each string, compare it with the longest common prefix.
#4. If the current string is smaller than the longest common prefix, update the longest common prefix.
#5. Return the longest common prefix.
#time complexity: O(n)
#space complexity: O(1)

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]