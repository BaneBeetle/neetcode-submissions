class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Our goal is to count islands where we cannot go out of boundary

        counter = 0
        seen = set()
        ROW = len(grid)
        COL = len(grid[0])

        r = 0
        while r < ROW:
            c = 0
            while c < COL:
                if grid[r][c] == 1 and (r, c) not in seen:
                    valid = True
                    queue = [(r, c)]
                    islands_seen = 1
                    seen.add((r, c))
                    while queue:
                        cr, cc = queue.pop()
                        for dr, dc in directions:
                            if 0 > cr + dr or cr + dr >= ROW or 0 > cc + dc or cc + dc >= COL:
                                valid = False
                            if 0 <= cr + dr < ROW and 0 <= cc + dc < COL and grid[cr+dr][cc+dc] == 1 and (cr+dr, cc+dc) not in seen: 
                                queue.append((cr+dr, cc+dc))
                                seen.add((cr+dr, cc+dc))
                                islands_seen += 1

                    if valid == True:
                        counter += islands_seen

                c += 1
            r += 1
        return counter