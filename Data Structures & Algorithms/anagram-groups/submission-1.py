class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            key = tuple(sorted(word))
            if key not in group:
                group[key] = []

            group[key].append(word)

        return list(group.values())

        # Time: O(m * nlogn)
        # Space: O(m*n) 
        # m is the number of strings and n is the max length string