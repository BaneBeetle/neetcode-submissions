from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0

        ROW = len(grid)
        COL = len(grid[0])
        r = 0
        queue = deque([])
        fresh = 0

        while r < ROW:
            c=0
            while c < COL:
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
                c +=1
            r += 1
        
        while queue and fresh > 0:
            queue_size = len(queue)
            for _ in range(queue_size):
                r, c = queue.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    if 0 <= r + dr < ROW and 0 <= c + dc < COL and grid[r+dr][c+dc] == 1:
                        queue.append((r + dr, c + dc))
                        grid[r + dr][c + dc] = 2
                        fresh -= 1
            time += 1
        if fresh:
            return -1
        return time
