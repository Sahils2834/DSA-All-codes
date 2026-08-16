#leetcode 67 : Add Binary
#input: a = "11", b = "1"
#output: "100"
#algorithm :
#1. start from the end of both strings
#2. add the digits and carry
#3. if sum is 2, set to 0 and carry 1
#4. if sum is 3, set to 1 and carry 1
#5. repeat until both strings are processed
#6. if carry remains, add it to the beginning
#time complexity: O(n)
#space complexity: O(n)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []
        while i>=0 or j>=0 or carry:
            sum = carry
            if i>=0:
                sum += int(a[i])
                i -= 1
            if j>=0:
                sum += int(b[j])
                j -= 1
            carry = sum // 2
            result.append(sum % 2)
        return "".join(result[::-1])