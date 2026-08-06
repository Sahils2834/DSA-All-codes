#Leetcode 3(Longest substring without repeating characters)
#algorithm = sliding window with left and right pointers; use a hash map to store last seen index of characters
#if char at right is in map, move left pointer to max(left, last_seen_index + 1)
#update max length and char's index in map on each iteration
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
