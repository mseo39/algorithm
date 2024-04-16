# 퍼즐 조각 채우기
"""
*문제에 그림이 많이 포함되어있으므로 문제로 이동

테이블 위에 놓인 퍼즐 조각을 게임 보드의 빈 공간에 적절히 올려놓으려 합니다. 
게임 보드와 테이블은 모두 각 칸이 1x1 크기인 정사각 격자 모양입니다. 이때, 다음 규칙에 따라 테이블 위에 놓인 퍼즐 조각을 게임 보드의 빈칸에 채우면 됩니다.

조각은 한 번에 하나씩 채워 넣습니다.
조각을 회전시킬 수 있습니다.
조각을 뒤집을 수는 없습니다.
게임 보드에 새로 채워 넣은 퍼즐 조각과 인접한 칸이 비어있으면 안 됩니다.
"""
from collections import deque

def solution(game_board, table):
    
    loc=[[-1,0],[0,1],[1,0],[0,-1]]
    h=len(game_board)
    puzzle=[]
    empty=[]
    
    answer = 0
    
    def bfs(origin,result: list,x,y,v,t):
        q=deque()
        q.append([x,y])
        origin[x][y]=t
        tmp=[[x,y]]
        
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx=x+loc[i][0]
                ny=y+loc[i][1]
                if 0<=nx<h and 0<=ny<h and origin[nx][ny]==v:
                    q.append([nx, ny])
                    origin[nx][ny]=t
                    tmp.append([nx,ny])

        min_x=min(tmp, key=lambda x:x[0])[0]
        min_y= min(tmp, key=lambda x:x[1])[1]
        
        for i in range(len(tmp)):
            tmp[i][0]-=min_x
            tmp[i][1]-=min_y
            
        max_x = max(tmp, key=lambda x:x[0])[0]+1
        max_y = max(tmp, key=lambda x:x[1])[1]+1

        matrix=[[0]*max_y for _ in range(max_x)]

        for x,y in tmp:
            matrix[x][y]=1
            
        result.append(matrix)

    def rotate(block):
        tmp=[[0]*len(block) for _ in range(len(block[0]))]
        for x in range(len(block)):
            for y in range(len(block[0])):
                tmp[y][len(block)-1-x]=block[x][y]
        return tmp
                    
    for x in range(h):
        for y in range(h):
            if table[x][y]==1:
                bfs(table, puzzle,x,y,1,0)
            if game_board[x][y]==0:
                bfs(game_board, empty,x,y,0,1)

    for i in puzzle:
        if i in empty:
            answer+=sum(k.count(1) for k in i)
            empty.remove(i)
            continue
        t=i
        for _ in range(3):
            t=rotate(t)
            if t in empty:
                answer+=sum(k.count(1) for k in i)
                empty.remove(t)
                break

    return answer

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
         [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
