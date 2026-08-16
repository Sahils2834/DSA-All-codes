#leetcode 58 : Length of Last Word
#input s= "Hello World"
#output= 5
#algorithm : 
#1. trim last space
#2. reverse string
#3. find first space
#4. length of string
#Eg: "Hello World" -> reverse -> "dlroW olleH"
#Eg 2:"Hello World" -> trim last space -> "Hello World"
#time complexity: O(n)
#space complexity: O(n)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        i = len(s) - 1
        length = 0
        while i>=0 and s[i] == " ":
            i-=1
        while i>=0 and s[i] != " ":
            length+=1
            i-=1
        return length

    