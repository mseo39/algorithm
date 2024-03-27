# 개리맨더링 2
"""

"""
import sys
from collections import deque

loc=[[1,0],[0,1],[-1,0],[0,-1]]

def bfs(arr,x, y, d1, d2):
    global result
    max_num=0
    min_num=400000

    visited=[[0 for _ in range(N)] for _ in range(N)]

    for v in range(4,-1,-1):
        if v==1:
            sX=0
            sY=0
            eX=x+d1-1
            eY=y
        elif v==2:
            sX=0
            sY=y+1
            eX=x+d2
            eY=N-1
        elif v==3:
            sX=x+d1
            sY=0
            eX=N-1
            eY= y-d1+d2-1
        elif v==4:
            sX=x+d2+1
            sY=y-d1+d2
            eX=N-1
            eY=N-1
        elif v==0:
            sX=x
            sY=y-1
            eX=x+d1+d2
            eY=y+d2

        q=deque()
        cnt=0
        if v==4:
            q.append([eX,eY])
            visited[eX][eY]=v
            cnt=A[eX][eY]
        elif v==3:
            q.append([eX,sY])
            visited[eX][sY]=v
            cnt=A[eX][sY]
        else:
            q.append([sX,sY])
        if v!=0 and v!=4 and v!=3:
            visited[sX][sY]=v
            cnt=A[sX][sY]

        while q:
            cX,cY = q.popleft()
            for l in loc:
                if sX<= cX+l[0] <=eX and sY<= cY+l[1] <=eY:
                    if (v==0 or arr[cX+l[0]][cY+l[1]]!=5) and visited[cX+l[0]][cY+l[1]]==0:
                        q.append([cX+l[0],cY+l[1]])
                        if v==0:
                            visited[cX+l[0]][cY+l[1]]=5
                        else:
                            visited[cX+l[0]][cY+l[1]]=v
                        cnt+=A[cX+l[0]][cY+l[1]]

        min_num=min(min_num,cnt)
        max_num=max(max_num,cnt)
        # print()
        # print(v, cnt)
        # for i in visited:
        #     print(*i)

    result=min(result,max_num-min_num)
    return

def line(x,y,d1,d2):
    visited=[[0 for _ in range(N)] for _ in range(N)]
    for i in range(d1+1):
        visited[x+i][y-i]=5
    for i in range(d2+1):
        visited[x+i][y+i]=5
    for i in range(d2+1):
        visited[x+d1+i][y-d1+i]=5
    for i in range(d1+1):
        visited[x+d2+i][y+d2-i]=5

    # print()
    # for i in visited:
    #     print(*i)
    bfs(visited,x,y,d1,d2)


N= int(sys.stdin.readline())
A=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
result=400000

for x in range(N-2):
    for y in range(1,N-1):
        for d1 in range(1, N-1):
            for d2 in range(1, N-1):
                if 0 <= x+d1-1 < N and 0 <= x+d2-1 < N and 0 <= y-d1+d2-1 < N:
                    if 0 <= y-d1 and y+d2 < N and x+d1+d2 < N:
                        line(x, y, d1, d2)
print(result)