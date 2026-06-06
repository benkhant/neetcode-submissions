class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtracking(closed, opened):
            if closed == opened == n:
                res.append("".join(stack))

            if opened < n:
                stack.append("(")
                backtracking(closed, opened + 1)
                stack.pop()

            if closed < opened:
                stack.append(")")
                backtracking(closed + 1, opened)
                stack.pop()

        backtracking(0, 0)
        return res

        # time: O(4^n / sqrt(n))
        # space: O(n)
            