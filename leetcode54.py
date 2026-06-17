#leetcode 54-Spiral Matrix(optimal solution)
#time complexity- O(n*m)
#space complexity- O(1)

class Solution(object):
    def spiralOrder(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        result = []

        while left <= right and top <= bottom:

            # Left -> Right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Top -> Bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Right -> Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # Bottom -> Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
        
        
