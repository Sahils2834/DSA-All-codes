#generate all possible paranthesis of a string of length 2n
#tc -- O(2^n)
#sc -- O(n)

class Solution(object):

    def solve(self, ind, brac, total, n, result):

        if total < 0:
            return

        if ind == len(brac):
            if total == 0:
                result.append("".join(brac))
            return

        open_used = brac[:ind].count("(")

        if open_used < n:
            brac[ind] = "("
            self.solve(ind + 1, brac, total + 1, n, result)

        if total > 0:
            brac[ind] = ")"
            self.solve(ind + 1, brac, total - 1, n, result)

    def generateParenthesis(self, n):
        result = []
        brac = [""] * (2 * n)

        self.solve(0, brac, 0, n, result)

        return result

