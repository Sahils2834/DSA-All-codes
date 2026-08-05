#Leetcode 3(Longest substring without repeating characters)
#algorithm = we will use the concept of sliding window
#time complexity = O(n)
#space complexity = O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_len = 0
        char_set = {}
        while right < len(s):
            if s[right] in char_set:
                left = max(left, char_set[s[right]] + 1)
            max_len = max(max_len, right - left + 1)
            char_set[s[right]] = right
            right += 1
        return max_len
