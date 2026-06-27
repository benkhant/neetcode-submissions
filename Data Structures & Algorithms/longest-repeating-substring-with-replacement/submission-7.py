class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        maxf = 0
        maxLength = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxf = max(maxf, freq[s[r]])
            if (r - l + 1) - maxf <= k:
                maxLength = max(maxLength, r - l + 1)
            else:
                freq[s[l]] -= 1
                l += 1
        return maxLength

        # Time: O(n)
        # Space: O(1)

        # maxLength = 0
        # for i in range(len(s)):
        #     freq = {}
        #     for j in range(i, len(s)):
        #         freq[s[j]] = freq.get(s[j], 0) + 1
        #         maxFreq = max(freq.values())
        #         if (j - i + 1) - maxFreq <= k:
        #             maxLength = max(maxLength, j - i + 1)
        # return maxLength

        # Time: O(n^2)
        # Space: O(m), m = numbers of unique characters