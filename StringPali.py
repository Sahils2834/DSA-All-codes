#check if string is palindrome using loops

s = "NITIN"
left = 0
right = len(s) - 1
is_palindrome = True

while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print(f"'{s}' is a palindrome")
else:
    print(f"'{s}' is not a palindrome")
