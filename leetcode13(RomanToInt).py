#leetcode 13 : Roman to Integer
#Algorithm
#1. Create a dictionary to store the values of Roman numerals.
#2. Iterate through the Roman numeral string from left to right.
#3. If the current numeral is smaller than the next numeral, subtract its value from the total.
#4. Otherwise, add its value to the total.
#5. Return the total.
#time complexity: O(n)
#space complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000 }
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                result -= values[s[i]]
            else:
                result += values[s[i]]
        return result