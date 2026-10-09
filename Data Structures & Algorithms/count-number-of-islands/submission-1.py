class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # we need a visited set, we need a returnable counter
        # Useful to have a ROWS COLS
        visited = set() # coordinates
        num_islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            # r is current row, c is current col

            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return
            

            if grid[r][c] == '0' or ((r, c) in visited):
                return

            visited.add((r, c))
            # explore up down left right
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        row = 0
        while row < ROWS:
            # Will go through the rows, no access to specific elements yet
            current_row = grid[row]
            col = 0
            while col < COLS:
                # Check whether the element is 0 or 1, if its a 1 -> DFS, else -> do nothing
                if current_row[col] == '1' and ((row, col) not in visited):
                    dfs(row, col)
                    num_islands += 1
                col += 1

            row += 1

        return num_islands
        