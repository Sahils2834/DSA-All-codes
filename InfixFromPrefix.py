#Infix From Prefix
#time complexity: O(n)
#space complexity: O(n)

#Algorithm:
#1. Initialize an empty stack.
#2. Iterate through each character of the prefix expression in reverse order:
#       a.If the character is an operand (letter or digit), push it onto the stack.
#       b.If the character is an operator, pop the top two operands from the stack.
#       c.Create a new string by concatenating the operator, the first popped operand, and the second popped operand, enclosed in parentheses: (operator operand1 operand2).
#       d.Push this new string back onto the stack.
#3. After iterating through the expression, the stack will contain a single element which is the infix expression.
#Example:
#Input: +ab*cd
#Output: (a+(b*(c*d)))

def InfixFromPrefix(prefix):
    stack = []
    for char in prefix[::-1]:
        if char.isalnum():
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append("(" + operand1 + char + operand2 + ")")
    return stack[0]
