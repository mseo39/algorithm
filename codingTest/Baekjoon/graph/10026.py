# 적록색약
"""
시간제한 1초
메모리제한 128MB

적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.
크기가 NxN인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다.
그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)
그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)
둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.
"""
import sys
from collections import deque
location=[[0,1],[1,0],[-1,0],[0,-1]]

def bfs(x,y,v,visited):
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    while q:
        x,y=q.popleft()
        for i in location:
            n_x=x+i[0]
            n_y=y+i[1]
            if 0<=n_x<N and 0<=n_y<N and visited[n_x][n_y]==0 and A[n_x][n_y] in v:
                q.append([n_x,n_y])
                visited[n_x][n_y]=1

N= int(sys.stdin.readline())
A= [sys.stdin.readline().strip() for _ in range(N)]
visited=[[0 for _ in range(N)] for _ in range(N)]
RG_visited=[[0 for _ in range(N)] for _ in range(N)]
R=0
G=0
B=0
RG=0

for x in range(N):
    for y in range(N):
        if visited[x][y]==0:
            if A[x][y]=="R":
                bfs(x,y,["R"],visited)
                R+=1
            if A[x][y]=="G":
                bfs(x,y,["G"],visited)
                G+=1
            if A[x][y]=="B":
                bfs(x,y,["B"],visited)
                B+=1
        if A[x][y] in ["R","G"] and RG_visited[x][y]==0:
            bfs(x,y,["R","G"],RG_visited)
            RG+=1
print(R+G+B, RG+B)