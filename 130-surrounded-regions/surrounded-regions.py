from collections import deque
class Solution(object):
    def solve(self, board):
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
            r,c=q.popleft()
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c]!="O":
                continue
            board[r][c]="#"
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                q.append((r+dr,c+dc))  
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="#":
                    board[r][c]="O"    



        