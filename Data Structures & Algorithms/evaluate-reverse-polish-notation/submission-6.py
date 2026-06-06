class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            if token not in "+-*/":
                stack.append(token)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token == "+":
                    res = num1 + num2
                elif token == "-":
                    res = num1 - num2
                elif token == "*":
                    res = num1 * num2
                elif token == "/":
                    res = int(num1 / num2)
                stack.append(res)
        return res