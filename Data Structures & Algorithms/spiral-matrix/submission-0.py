class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        ROW = len(matrix)
        COL = len(matrix[0])
        seen = set()

        r = 0
        c = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        while len(ret) < ROW*COL:
            if (r, c) not in seen:
                ret.append(matrix[r][c])
                seen.add((r, c))
            dr, dc = directions[d]

            if 0 <= r+dr < ROW and 0 <= c+dc < COL and (r+dr, c+dc) not in seen:
                r += dr
                c += dc
            else:
                # invalid
                d = (d + 1) % 4

        return ret
