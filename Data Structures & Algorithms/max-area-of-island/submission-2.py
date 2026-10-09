class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from collections import deque

        # max_area can be updated once a BFS is fully complete
        
        visited = set() # Keep track of what we have seen

        max_area = 0

        row = len(grid)
        col = len(grid[0])

        queue = deque()

        r = 0
        while r < row:
            c = 0
            while c < col:

                if grid[r][c] == 1 and (r, c) not in visited:
                    queue.append((r, c))
                    current_area = 0
                    visited.add((r, c))

                    while queue:
                        visit = queue.popleft() # What we are visiting rn
                        current_area += 1

                        neighbors = [(visit[0] - 1, visit[1]), 
                        (visit[0] + 1, visit[1]), (visit[0], visit[1] - 1),
                        (visit[0], visit[1] + 1)]

                        for coords in neighbors:
                            if 0 <= coords[0] < row and 0 <= coords[1] < col:
                                # If its in range
                                if grid[coords[0]][coords[1]] == 1 and coords not in visited:
                                    # If its a valid island
                                    queue.append(coords)
                                    visited.add(coords)
                    
                    max_area = max(max_area, current_area) # Update global max

                c += 1
            r += 1

        return max_area
        