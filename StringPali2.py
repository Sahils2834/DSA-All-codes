#check if string is palindrome using recursion 
s=""

def func(s,left,right):
    if left >= right:
         return True 
    if s[left] != s[right]:
        return False
    return func(s,left+1, right-1)
