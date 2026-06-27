class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        for i in range(len(s)):
            freq = {}
            for j in range(i, len(s)):
                freq[s[j]] = freq.get(s[j], 0) + 1
                maxFreq = max(freq.values())
                if (j - i + 1) - maxFreq <= k:
                    maxLength = max(maxLength, j - i + 1)
        return maxLength

        # Time: O(n^2)
        # Space: O(m), m = numbers of unique characters