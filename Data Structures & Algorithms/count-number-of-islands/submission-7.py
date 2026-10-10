class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROW = len(grid)
        COL = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0
        seen = set()
        queue = []

        row = 0
        col = 0

        while row < ROW:
            col = 0
            while col < COL:

                if grid[row][col] == "1" and (row, col) not in seen:
                    queue.append((row, col))
                    while queue:
                        curr_row, curr_col = queue.pop()
                        seen.add((curr_row, curr_col))
                        for dr, dc in directions:
                            if 0 <= (curr_row + dr) < ROW and 0 <= (curr_col + dc) < COL and grid[curr_row + dr][curr_col + dc] == "1" and (curr_row + dr, curr_col + dc) not in seen:
                                queue.append((curr_row + dr, curr_col + dc))
                    islands += 1
                col += 1
            row += 1

        return islands
