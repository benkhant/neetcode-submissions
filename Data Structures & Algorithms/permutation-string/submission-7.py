class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2)):
            if sorted(s1) == sorted(s2[i:i + len(s1)]):
                    return True
        return False

    # Time: O(n^2logn)
    # Space: O(n)