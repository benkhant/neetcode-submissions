class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for c in strs:
                if i == len(c) or c[i] != strs[0][i]:
                    return c[:i]
        return strs[0]