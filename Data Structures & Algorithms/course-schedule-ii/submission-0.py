class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        preq = { c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preq[crs].append(pre)

        visited = set()
        cycle = set()

        def dfs(c):
            if c in cycle:
                return False

            if c in visited:
                return True

            cycle.add(c)

            for pre in preq[c]:
                if not dfs(pre):
                    return False

            cycle.remove(c)
            visited.add(c)
            res.append(c)

            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res

        # time: O(V + E)
        # space: O(V + E)
