class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for neighbour in adj[node]:
                dfs(neighbour)
        
        count = 0
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)
        return count

        # Time: O(V+E)
        # Space: O(V+E)