#leetcode 51 n queens
#tc=o(n!)
#sc=o(n)

class Solution:
    def solve(self, col, board, ans, leftrow, upperD, lowerD, n):
        if col == n:
            ans.append(board[:])
            return

        for row in range(n):
            if( leftrow[row] == 0 and lowerD[col + row] == 0 and upperD[n-1 + col - row] == 0):
                board[row]= board[row][:col] + "Q" + board[row][col + 1 :]
                leftrow[row] = 1
                lowerD[col+ row] = 1
                upperD[n-1 + col - row] = 1
                self.solve(col + 1, board, ans, leftrow, upperD, lowerD, n)
                board[row] = board[row][:col] + "." + board[row][col + 1:]
                leftrow[row] = 0
                lowerD[col+ row] = 0
                upperD[n-1 + col - row] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ["." * n for _ in range(n)]
        leftrow = [0] * n
        lowerD = [0] * (2 * n - 1)
        upperD = [0] * (2 * n - 1)
        self.solve(0, board, ans, leftrow, upperD, lowerD, n)
        return ans