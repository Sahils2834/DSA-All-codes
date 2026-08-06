#Infix To Postfix
#time complexity: O(n)
#space complexity: O(n)
#Algorithm:
#1.Initialize an empty stack and an empty list for postfix expression.
#2.Iterate through each character in the infix expression:
#       a.If the character is an operand (letter or digit), append it to the postfix list.
#       b.If the character is '(', push it onto the stack.
#       c.If the character is ')', pop from the stack and append to the postfix list until '(' is encountered. Discard both parentheses.
#       d.If the character is an operator, compare its precedence with the top of the stack. Pop and append operators from the stack to the postfix list if they have higher or equal precedence. Then push the current operator onto the stack.
#3.After iterating through the expression, pop any remaining operators from the stack and append them to the postfix list.
#4.Join the postfix list to form the final postfix expression string.


def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/':
        return 2
    if operator == '^':
        return 3
    return 0

def infixToPostfix(infix):
    stack = []
    postfix = []
    for char in infix:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':   
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':  
                postfix.append(stack.pop())
            stack.pop()  
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())
    return "".join(postfix)
