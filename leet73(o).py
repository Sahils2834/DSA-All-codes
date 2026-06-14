#leetcode 73- Set Matrix Zeroes(optimal solution)
#time complexity- O(n*m)
#space complexity- O(1)

class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        rowtrack = [0 for _ in range(rows)]
        coltrack = [0 for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowtrack[i] = -1
                    coltrack[j] = -1

        for i in range(rows):
            for j in range(cols):
                if rowtrack[i] == -1 or coltrack[j] == -1:
                    matrix[i][j] = 0