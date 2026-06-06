class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for ch in t: 
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1
        
        best = ""

        if len(s) < len(t):
            return ""

        for i in range(len(s)):
            have = {}
            for j in range(i, len(s)):
                have[s[j]] = have.get(s[j], 0) + 1
                valid = True
                for ch in need:
                    if have.get(ch, 0) < need[ch]:
                        valid = False
                        break

                if valid:
                    if best == "" or len(s[i:j+1]) < len(best):
                        best = s[i:j+1]
                    break
        return best

        # time: O(n^2 * len(t))
        # space: O(n)