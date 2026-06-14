#leetcode 73- Set Matrix Zeroes(brute force solution)
#time complexity- O(n*m)
#space complexity- O(n*m)

class Solution(object):
    def mark_infi(self, matrix, row, col):
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            if matrix[i][col] != 0:
                matrix[i][col] = float("inf")

        for j in range(cols):
            if matrix[row][j] != 0:
                matrix[row][j] = float("inf")

    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    self.mark_infi(matrix, i, j)

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0