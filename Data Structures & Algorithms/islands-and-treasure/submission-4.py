from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Phase 1, scan for all treasures and add them to the queue
        ROW = len(grid)
        COL = len(grid[0])
        r = 0

        queue = deque([])
        while r < ROW:
            c = 0
            while c < COL:
                if grid[r][c] == 0:
                    queue.append((r, c))
                c += 1
            r += 1

        # Phase 2, BFS. We add neighbor IF not -1.
        # While updating values, we would take the min(proposed, whatever it is)
        count = 0
        while queue:
            queue_length = len(queue)
         
            for _ in range(queue_length):
                r, c = queue.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    if 0 <= r + dr < ROW and 0 <= c + dc < COL and grid[r+dr][c+dc] == 2147483647:
                        grid[r+dr][c+dc] = count + 1
                        queue.append((r+dr, c+dc))

            count += 1


