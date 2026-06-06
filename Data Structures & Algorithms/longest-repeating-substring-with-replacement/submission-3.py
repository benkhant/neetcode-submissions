class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        max_count = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_count = max(count[s[r]], max_count)
            while r - l + 1 - max_count > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
                
        return res 

        # time: O(n)
        # space: O(m)

        # res = 0
        # for i in range(len(s)):
        #     freq = {}
        #     for j in range(i, len(s)):
        #         freq[s[j]] = freq.get(s[j], 0) + 1
        #         max_freq = max(freq.values())
        #         length = j - i + 1
        #         if length - max_freq <= k:
        #             res = max(res, length)
        # return res

        # time: O(n^2)
        # space: O(m)