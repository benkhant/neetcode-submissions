class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0 

        for i in range(n):
            # odd case
            count += self.countPali(s, i, i)

            # even case
            count += self.countPali(s, i, i + 1)
        return count

    def countPali(self, s, l, r):
        n = len(s)
        count = 0
        while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count
        
        # time: O(n^2)
        # space: O(1)