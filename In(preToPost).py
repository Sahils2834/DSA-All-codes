#Prefix To Postfix
#time complexity: O(n)
#space complexity: O(n)

#Algorithm:
#1. Initialize an empty stack.
#2. Iterate through each character of the prefix expression in reverse order:
#       a.If the character is an operand (letter or digit), push it onto the stack.
#       b.If the character is an operator, pop the top two operands from the stack.
#       c.Create a new string by concatenating the first popped operand, the second popped operand, and the operator, enclosed in parentheses: (operand1 operator operand2).
#       d.Push this new string back onto the stack.
#3. After iterating through the expression, the stack will contain a single element which is the postfix expression.
#Example:
#Input: +ab
#Output: ab+

class solution:
    def preToPost(self,prefix:str)->str:
        stack = []
        for char in prefix[::-1]:
            if char.isalnum():
                stack.append(char)
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(operand1 + operand2 + char)
        return stack[0]