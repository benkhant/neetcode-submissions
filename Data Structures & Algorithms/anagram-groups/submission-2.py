class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(word)
        return list(res.values())

        # Time: O(m*n)
        # Space: O(m*n)

        # group = {}
        # for word in strs:
        #     key = tuple(sorted(word))
        #     if key not in group:
        #         group[key] = []

        #     group[key].append(word)

        # return list(group.values())

        # Time: O(m * nlogn)
        # Space: O(m*n) 
        # m is the number of strings and n is the max length string