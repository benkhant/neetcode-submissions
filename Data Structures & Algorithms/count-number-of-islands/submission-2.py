class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        visit = set()

        # bfs
        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dc, dr in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and 
                        c in range(COLS) and 
                        grid[r][c] == "1" and
                       (r, c) not in visit):
                       q.append((r, c))
                       visit.add((r, c))
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands


        # dfs
        # def dfs(r, c):
        #     if (not grid or 
        #         r < 0 or c < 0 or
        #         r == ROWS or c == COLS or
        #         grid[r][c] != '1'):
        #         return 0

        #     grid[r][c] = "0"
        #     for dr, dc in directions:
        #         dfs(r + dr, c + dc)
            
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == "1":
        #             dfs(r, c)
        #             islands += 1
        # return islands