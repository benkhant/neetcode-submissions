class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for ch in t: 
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1
        
        r = 0
        have = 0
        window = {}
        needCount = len(need)
        res = [-1, -1]
        resLen = float('inf')
        l = 0

        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in need and window[s[r]] == need[s[r]]:
                have += 1

            while have == needCount:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
            r += 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""

        # need = {}
        # for ch in t: 
        #     if ch in need:
        #         need[ch] += 1
        #     else:
        #         need[ch] = 1
        
        # best = ""

        # if len(s) < len(t):
        #     return ""

        # for i in range(len(s)):
        #     have = {}
        #     for j in range(i, len(s)):
        #         have[s[j]] = have.get(s[j], 0) + 1
        #         valid = True
        #         for ch in need:
        #             if have.get(ch, 0) < need[ch]:
        #                 valid = False
        #                 break

        #         if valid:
        #             if best == "" or len(s[i:j+1]) < len(best):
        #                 best = s[i:j+1]
        #             break
        # return best

        # time: O(n^2 * len(t))
        # space: O(n)