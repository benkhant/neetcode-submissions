class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nr == ROWS or nc < 0 or nc == COLS or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
               
            time += 1
        return time if fresh == 0 else -1

        # time: O(m*n)
        # space: O(m*n)