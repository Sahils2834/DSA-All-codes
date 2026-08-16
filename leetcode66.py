#leetcode 66 : Plus One
#input: digits = [1,2,3]
#output: [1,2,4]
#algorithm :
#1. increment last digit
#2. if last digit is 10, set it to 0 and increment previous digit
#3. repeat until no carry
#4. if carry remains, add it to the beginning
#time complexity: O(n)
#space complexity: O(n)

class solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[i] < 9:
               digits[i] += 1
               return digits
            digits[i] = 0
        return [1] + digits
            