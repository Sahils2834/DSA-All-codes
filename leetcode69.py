#leetcode 69 : Sqrt of x
#input: x = 4
#output: 2
#algorithm :
#1. Use binary search to find the square root
#2. If mid*mid == x, return mid
#3. If mid*mid < x, search in the right half
#4. If mid*mid > x, search in the left half
#time complexity: O(log n)
#space complexity: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
        
        left = 1
        right = x//2
        answer = 0


        while left <= right:
            mid = (left + right)//2

            if mid*mid == x:
                return mid
            
            elif mid*mid < x:
                answer = mid
                left = mid + 1
            
            else:
                right = mid - 1
        
        return answer
                

    
    