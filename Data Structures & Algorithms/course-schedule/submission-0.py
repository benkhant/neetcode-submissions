class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = len(prerequisites)
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[b].append(a)

        visiting = set()
        visited = set()

        def dfs(c):

            if c in visiting:
                return False
            
            if c in visited:
                return True

            visiting.add(c)

            for nei in adj[c]:
                if not dfs(nei):
                    return False

            visiting.remove(c)
            visited.add(c)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
