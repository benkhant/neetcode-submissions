class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    maxLength = max(maxLength, j - i + 1)
                else:
                    break
        return maxLength

        # Time: O(n^2)
        # Space: O(1)