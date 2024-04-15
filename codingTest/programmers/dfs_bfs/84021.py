from collections import deque

def solution(game_board, table):
    
    loc=[[-1,0],[0,1],[1,0],[0,-1]]
    h=len(game_board)
    puzzle=[]
    empty=[]
    
    answer = 0
    
    def bfs(origin,result,x,y,v,t):
        q=deque()
        q.append([x,y])
        origin[x][y]=t
        d=[]
        
        while q:
            x,y = q.popleft()
            tmp=[]
            for i in range(4):
                nx=x+loc[i][0]
                ny=y+loc[i][1]
                if 0<=nx<h and 0<=ny<h and origin[nx][ny]==v:
                    q.append([nx, ny])
                    origin[nx][ny]=t
                    tmp.append(i)
            d.append(tmp)
            
        if d:
            result.append(d)
                    
    for x in range(h):
        for y in range(h):
            if table[x][y]==1:
                bfs(table, puzzle,x,y,1,0)
            if game_board[x][y]==0:
                bfs(game_board, empty,x,y,0,1)
                
    print(puzzle)
    print(empty)
    
    # 90도 회전하면서 일치하는거 찾기
    for p in puzzle:
        print()
        print(p)
        if p in empty:
            answer+=sum(len(t) for t in p)
            empty.remove(p)
            continue
        for i in range(1,4):
            print([list(map(lambda x : (x+i)%4,t)) for t in p])
            if [list(map(lambda x : (x+i)%4,t)) for t in p] in empty:
                answer+=sum(len(t) for t in p)
                empty.remove([list(map(lambda x : (x+i)%4,t)) for t in p])
                break
    print(answer)
    return answer

solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
         [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])
