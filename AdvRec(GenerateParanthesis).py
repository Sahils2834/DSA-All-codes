#generate all possible paranthesis of a string of length 2n
#algorithm = use recursion; at each position we have two choices: place '(' or ')'
#place '(' only if count of open brackets used so far < n
#place ')' only if current open bracket count (total) > 0 (meaning there's an unmatched '(' to close)
#when the index reaches 2n and total == 0 (all brackets matched), add to result
#if total < 0 at any point, backtrack (invalid state)
#tc -- O(4^n / sqrt(n)) (Catalan number) approximated as O(2^n)
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

