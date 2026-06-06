class Solution:
    def isHappy(self, n: int) -> bool:

        def helper(n):
            total = 0
            while n:
                digit = n % 10
                digit = digit ** 2
                total += digit
                n = n // 10
            return total
        
        visit = set()
        while n not in visit:
            visit.add(n)
            n = helper(n)
            if n == 1: 
                return True
        return False

        # time: O(logn)
        # space: O(logn)