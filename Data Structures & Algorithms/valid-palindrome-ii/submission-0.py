class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        def isPalin(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return isPalin(i+1, j) or isPalin(i, j-1)
        return True

        # Time: O(n)
        # Space: O(1)