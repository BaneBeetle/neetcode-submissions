class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        most = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        ROW = len(grid)
        COL = len(grid[0])

        seen = set()

        r = 0
    
        while r < ROW:
            c = 0
            while c < COL:

                if grid[r][c] == 1:
                    queue = [(r, c)]
                    count = 0
                    seen.add((r, c))
                    while queue:
                        cr, cc = queue.pop()
                        count += 1
                        
                        for dr, dc in directions:
                            x = cr + dr
                            y = cc + dc

                            if 0 <= x < ROW and 0 <= y < COL and (x, y) not in seen and grid[x][y] == 1:
                                seen.add((x, y))
                                queue.append((x, y))
                    most = max(most, count)

                c += 1
            r += 1


        return most