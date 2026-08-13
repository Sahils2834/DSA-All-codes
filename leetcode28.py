#leetcode 28 (find the index of the first occurrence in a string)
#algorithm
    #use two pointer approach
#time- O(n)
#space- O(1)

class solution:
    def strStr(self,haystack,needle):

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
            
        return -1
