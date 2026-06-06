class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        n = len(s)
        seen = set()
        res = 0

        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
        return res

        # time: O(n)
        # space: O(1)

        # n = len(s)
        # res = 0
        # for i in range(n):
        #     seen = set()
        #     for j in range(i, n):
        #         if s[j] in seen:
        #             break
        #         seen.add(s[j])
        #         res = max(res, j - i + 1)
                
        # return res

        # time: O(n^2)
        # space: O(n)