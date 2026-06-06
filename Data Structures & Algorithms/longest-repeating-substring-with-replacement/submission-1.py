class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            freq = {}
            for j in range(i, len(s)):
                freq[s[j]] = freq.get(s[j], 0) + 1
                max_freq = max(freq.values())
                length = j - i + 1
                if length - max_freq <= k:
                    res = max(res, length)
        return res

        # time: O(n^2)
        # space: O(m)