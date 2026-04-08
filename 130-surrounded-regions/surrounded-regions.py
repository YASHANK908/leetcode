from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        rows,cols=len(board),len(board[0])
        q=deque()

        for r in range(rows):
            for c in [0,cols-1]:
                if board[r][c]=="O":
                    q.append((r,c))
        for c in range(cols):
            for r in [0,rows-1]:
                if board[r][c]=="O":
                    q.append((r,c))
            
        while q:
            row,col=q.popleft()
            if row<0 or col<0 or row>=rows or col>=cols or board[row][col]!="O":
                continue
            board[row][col]="#"
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                q.append((row+dr,col+dc))
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="#":
                    board[r][c]="O"
                elif board[r][c]=="O":
                    board[r][c]="X"
         

                
                

        
        
        