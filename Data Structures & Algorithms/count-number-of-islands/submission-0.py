class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # we need a visited set, we need a returnable counter
        # Useful to have a ROWS COLS
        self.visited = set() # coordinates
        self.num_islands = 0
        self.ROWS = len(grid)
        self.COLS = len(grid[0])

        def dfs(r, c, grid):
            # r is current row, c is current col
            if r < 0 or c < 0 or r >= self.ROWS or c >= self.COLS:
                return
            element = grid[r][c]

            if element == '0':
                return
            else:
                # will hit if its a 1, add alll directions
                if (r, c) not in self.visited:
                    self.visited.add((r, c))
                    # explore up down left right
                    up = dfs(r + 1, c, grid)
                    down = dfs(r - 1, c, grid)
                    left = dfs(r, c - 1, grid)
                    right = dfs(r, c + 1, grid)

                return

        row = 0
        while row < self.ROWS:
            # Will go through the rows, no access to specific elements yet
            current_row = grid[row]
            col = 0

            while col < self.COLS:

                element = current_row[col]

                # Check whether the element is 0 or 1, if its a 1 -> DFS, else -> do nothing
                if element == '1' and ((row, col) not in self.visited):
                    dfs(row, col, grid)
                    self.num_islands += 1
                col += 1

            row += 1

        # We need to go through every row
        # We need to go through every element in that row
        # If the element is 1, run DFS
        # While DFS, Every new -> visited
        # Make sure its inbounds, if its a 0, also stop
        return self.num_islands
        