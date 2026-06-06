class Solution:
    def myPow(self, x: float, n: int) -> float:
        # res = x ** n
        # return res
        res = 1

        for i in range(abs(n)):
            res *= x
        
        if n < 0:
            return 1/res
        else:
            return res