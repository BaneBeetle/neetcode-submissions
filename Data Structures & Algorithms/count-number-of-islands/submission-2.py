class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set() # store seen coordinates

        num_islands = 0

        row = len(grid)
        col = len(grid[0])

        r = 0
        c = 0

        while r < row:
            while c < col:
                # Check if it is 1

                if grid[r][c] == '1' and (r, c) not in visited:

                    num_islands += 1
                    stack = [(r, c)]
                    while stack:
                        current = stack.pop()
                        visited.add(current)
                        neighbors = [(current[0], current[1] - 1), (current[0], current[1] + 1), (current[0] - 1, current[1]), (current[0] + 1, current[1])]

                        for coords in neighbors:
                            if 0 <= coords[0] < row and 0 <= coords[1] < col and coords not in visited and grid[coords[0]][coords[1]] == '1':
                                stack.append(coords)
                c += 1
            c = 0
            r += 1


        return num_islands
        