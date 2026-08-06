#leetcode 20-valid parentheses
#algorithm = use a stack and a hash map for matching pairs
#if char is a closing bracket, check if stack is empty or top doesn't match; if so, invalid
#otherwise, pop the matching opening bracket from stack
#if char is an opening bracket, push to stack
#valid if stack is empty at the end
# Time complexity: O(n) 
# Space complexity: O(n) 

class Solution():
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for bracket in s:
#             if bracket == "(" or bracket == "{" or bracket == "[":
#                 stack.append(bracket)
#             else:
#                 if len(stack) == 0:
#                     return False
#                 ch = stack.pop()
#                 if ((bracket == ")" and ch == "(") or
#                     (bracket == "}" and ch == "{") or
#                     (bracket == "]" and ch == "[")):
#                     continue
#                 else:
#                     return False
#         return len(stack) == 0