#leetcode 48-Rotate Image(brute force)
#algorithm = create a new result matrix of the same size
#map each element matrix[i][j] to result[j][n-1-i]
#time complexity- O(n*n)
#space complexity- O(n*n)

class Solution(object):
    def rotate(self, matrix):
      n = len(matrix)
      result = [[0 for _ in range(n)]for _ in range(n)]

      for i in range(n):
        for j in range(n):
          result[j][n-1-i] = matrix[i][j]
      return result

      