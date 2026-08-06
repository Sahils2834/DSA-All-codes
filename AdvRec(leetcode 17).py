#leetcode 17 letter combiantion of phone numbers 
#algorithm = map each digit to its letters (like a phone keypad)
#use backtracking: at each index, iterate over all letters mapped to digits[index]
#add the letter to subset and recurse to the next index
#backtrack by popping the letter after the recursive call
#base case: when index == len(digits), join subset and add to result
#Tc=o(4^n)
#sc=o(n)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def solve(index, subset):
            if index == len(digits):
                result.append("".join(subset))
                return

            for ch in char_map[digits[index]]:
                subset.append(ch)
                solve(index + 1, subset)
                subset.pop()

        solve(0, [])
        return result