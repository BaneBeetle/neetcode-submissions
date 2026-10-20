class Solution:

    def dfs(self, queue, visited, heights, ROW, COL):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        

        while queue:
            r, c = queue.pop()

            for dr, dc in directions:
                if 0 <= r + dr < ROW and 0 <= c + dc < COL and heights[r+dr][c+dc] >= heights[r][c] and (r+dr, c+dc) not in visited:
                    queue.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))

        return visited
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])
        

        pacific_queue = list(set([(x, 0) for x in range(ROW)] + [(0, z) for z in range(COL)]))
        atlantic_queue = list(set([(ROW-1, x) for x in range(COL)] + [(z, COL-1) for z in range(ROW)]))


        pacific_set = self.dfs(pacific_queue, set(pacific_queue), heights, ROW, COL)
        atlantic_set = self.dfs(atlantic_queue, set(atlantic_queue), heights, ROW, COL)

        return list(pacific_set.intersection(atlantic_set))





        
        