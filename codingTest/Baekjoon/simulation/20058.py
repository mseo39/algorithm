# 마법사 상어와 파이어스톰
"""
시간제한 1초
메모리 제한 512MB

마법사 상어는 파이어볼과 토네이도를 조합해 파이어스톰을 시전할 수 있다. 
오늘은 파이어스톰을 크기가 2**N x 2**N인 격자로 나누어진 얼음판에서 연습하려고 한다. 

위치 (r, c)는 격자의 r행 c열을 의미하고, 
A[r][c]는 (r, c)에 있는 얼음의 양을 의미한다. 
A[r][c]가 0인 경우 얼음이 없는 것이다.

파이어스톰을 시전하려면 시전할 때마다 단계 L을 결정해야 한다. 
파이어스톰은 먼저 격자를 2**L x 2**L 크기의 부분 격자로 나눈다. 
그 후, 모든 부분 격자를 시계 방향으로 90도 회전시킨다. 
이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다. 
(r, c)와 인접한 칸은 (r-1, c), (r+1, c), (r, c-1), (r, c+1)이다. 아래 그림의 칸에 적힌 정수는 칸을 구분하기 위해 적은 정수이다.

		
마법을 시전하기 전	L = 1	L = 2
마법사 상어는 파이어스톰을 총 Q번 시전하려고 한다. 모든 파이어스톰을 시전한 후, 다음 2가지를 구해보자.

남아있는 얼음 A[r][c]의 합
남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
얼음이 있는 칸이 얼음이 있는 칸과 인접해 있으면, 두 칸을 연결되어 있다고 한다. 덩어리는 연결된 칸의 집합이다.

입력
첫째 줄에 N과 Q가 주어진다. 둘째 줄부터 2N개의 줄에는 격자의 각 칸에 있는 얼음의 양이 주어진다. 
r번째 줄에서 c번째 주어지는 정수는 A[r][c] 이다.

마지막 줄에는 마법사 상어가 시전한 단계 L1, L2, ..., LQ가 순서대로 주어진다.

출력
첫째 줄에 남아있는 얼음 A[r][c]의 합을 출력하고, 둘째 줄에 가장 큰 덩어리가 차지하는 칸의 개수를 출력한다. 
단, 덩어리가 없으면 0을 출력한다
"""
import sys
from collections import deque

loc=[[0,1],[1,0],[-1,0],[0,-1]]


def chk_ice():
    ice=[]
    for x in range(2**N):
        for y in range(2**N):
            if A[x][y]>0:
                cnt=0
                for l in loc:
                    nX=x+l[0]
                    nY=y+l[1]
                    if 0<=nX<2**N and 0<=nY<2**N and A[nX][nY]>0:
                        cnt+=1
                if cnt<3:
                    ice.append([x,y])
    for i in ice:
        A[i[0]][i[1]]-=1

def bfs(x,y):
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    cnt=1

    while q:
        x,y = q.popleft()
        for l in loc:
            nX=x+l[0]
            nY=y+l[1]
            if 0<=nX<2**N and 0<=nY<2**N and visited[nX][nY]==0 and A[nX][nY]>0:
                cnt+=1
                visited[nX][nY]=1
                q.append([nX,nY])
    return cnt


N ,Q = map(int, sys.stdin.readline().strip().split())
A= [list(map(int, sys.stdin.readline().strip().split())) for _ in range(2**N)]

for L in map(int, sys.stdin.readline().strip().split()):
    tmp=[[0 for _ in range(2**N)] for _ in range(2**N)]
    for x in range(0,2**N,2**L):
        for y in range(0,2**N,2**L):
            for i in range(2**L):
                for j in range(2**L):
                    tmp[x+i][y+j]=A[x+2**L-1-j][y+i]

    A=tmp
    chk_ice()

#얼음의 총합
print(sum([sum(i) for i in A]))
#가장 큰 덩어리의 개수
max_cnt=0
visited=[[0 for _ in range(2**N)] for _ in range(2**N)]
for x in range(2**N):
    for y in range(2**N):
        if visited[x][y]==0 and A[x][y]>0:
            max_cnt=max(max_cnt, bfs(x,y))
print(max_cnt)