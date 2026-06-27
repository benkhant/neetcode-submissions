class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        maxLength = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        return maxLength

        # Time: O(n)
        # Space: O(m), m = numbers of unique characters

        # maxLength = 0
        # for i in range(len(s)):
        #     seen = set()
        #     for j in range(i, len(s)):
        #         if s[j] not in seen:
        #             seen.add(s[j])
        #             maxLength = max(maxLength, j - i + 1)
        #         else:
        #             break
        # return maxLength

        # Time: O(n^2)
        # Space: O(n)