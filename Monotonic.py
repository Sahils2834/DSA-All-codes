#Next Greater Element

#Algorithm:
#1. Initialize an empty stack.
#2. Iterate through each character of the array in reverse order:
#       a.If the character is an operand (letter or digit), push it onto the stack.
#       b.If the character is an operator, pop the top two operands from the stack.
#       c.Create a new string by concatenating the operator, the first popped operand, and the second popped operand, enclosed in parentheses: (operator operand1 operand2).
#       d.Push this new string back onto the stack.
#3. After iterating through the expression, the stack will contain a single element which is the infix expression.
#Example:
#Input: 4,5,2,10
#Output: 5,10,10,-1


def nextGreaterElement(nums):
    stack = []
    result = []
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if len(stack) != 0:
            result[i] = stack[-1]
        stack.append(nums[i])
    return result