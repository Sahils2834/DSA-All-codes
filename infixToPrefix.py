#Infix To Prefix

#Algorithm:
#1. Initialize an empty stack and an empty list for prefix expression.
#2. Reverse the infix expression.
#3. Iterate through each character of the reversed infix expression:
#       a.If the character is an operand (letter or digit), append it to the prefix list.
#       b.If the character is ')', push it onto the stack.
#       c.If the character is '(', pop from the stack and append to the prefix list until ')' is encountered. Discard both parentheses.
#       d.If the character is an operator, compare its precedence with the top of the stack. Pop and append operators from the stack to the prefix list if they have higher or equal precedence. Then push the current operator onto the stack.
#4. After iterating through the expression, pop any remaining operators from the stack and append them to the prefix list.
#5. Reverse the prefix list to form the final prefix expression string.

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/':
        return 2
    if operator == '^':
        return 3
    return 0

def infixToPrefix(infix):
    stack = []
    prefix = []
    infix = infix[::-1]
    for char in infix:
        if char.isalnum():
            prefix.append(char)
        elif char == ')':   
            stack.append(char)
        elif char == '(':  
            while stack and stack[-1] != ')':  
                prefix.append(stack.pop())
            stack.pop()  
        else:
            while stack and precedence(stack[-1]) > precedence(char):
                prefix.append(stack.pop())
            stack.append(char)

    while stack:
        prefix.append(stack.pop())
    return "".join(prefix[::-1])