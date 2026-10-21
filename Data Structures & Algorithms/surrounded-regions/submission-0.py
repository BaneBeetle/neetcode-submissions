class Solution:

    def valid(self, r, c, ROW, COL, board, seen):
        return 0 <= r < ROW and 0 <= c < COL and board[r][c] == "O" and (r, c) not in seen
    def solve(self, board: List[List[str]]) -> None:
        ROW = len(board)
        COL = len(board[0])
        
        queue = list(set([(0, c) for c in range(COL) if board[0][c] == "O"] + [(r, 0) for r in range(ROW) if board[r][0] == "O"] + [(ROW - 1, c) for c in range(COL) if board[ROW-1][c] == "O"] + [(r, COL-1) for r in range(ROW) if board[r][COL-1] == "O"]))

        visited = set(queue)
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.pop()

            for dr, dc in directions:
                if self.valid(r+dr, c+dc, ROW, COL, board, visited):
                    queue.append((r+dr, c+dc))
                    visited.add((r+dr, c+dc))

        
        r = 0
  
        while r < ROW:
            c=0
            while c < COL:
                if (r, c) not in visited and board[r][c] == "O":
                    board[r][c] = "X"

                c += 1    
            r += 1