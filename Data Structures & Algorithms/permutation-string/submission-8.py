class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq1 = {}
        freq2 = {}
        l = 0
        for i in range(len(s1)):
            freq1[s1[i]] = freq1.get(s1[i], 0) + 1
        
        for j in range(len(s2)):
            freq2[s2[j]] = freq2.get(s2[j], 0) + 1
            if (j - l + 1) > len(s1):
                freq2[s2[l]] -= 1
                if freq2[s2[l]] == 0:
                    del freq2[s2[l]]
                l += 1
            if freq1 == freq2:
                return True
        return False

        # Time: O(n), where n = len(s2)
        # Space: O(m), where m = len(s1), bounded by alphabet size in practice

        # for i in range(len(s2)):
        #     if sorted(s1) == sorted(s2[i:i + len(s1)]):
        #             return True
        # return False

    # Time: O(n * m log m), where n = len(s2), m = len(s1)
    # Space: O(m)