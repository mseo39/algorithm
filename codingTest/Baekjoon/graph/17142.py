#연구소 3
"""
시간제한 0.25초
메모리제한 512MB

인체에 치명적인 바이러스를 연구하던 연구소에 승원이가 침입했고, 바이러스를 유출하려고 한다. 
바이러스는 활성 상태와 비활성 상태가 있다. 가장 처음에 모든 바이러스는 비활성 상태이고, 
활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다. 
승원이는 연구소의 바이러스 M개를 활성 상태로 변경하려고 한다.
연구소는 크기가 NxN인 정사각형으로 나타낼 수 있으며, 정사각형은 1x1 크기의 정사각형으로 나누어져 있다. 
연구소는 빈 칸, 벽, 바이러스로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 
활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자. 0은 빈 칸, 1은 벽, 2는 바이러스의 위치이다.
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2

M = 3이고, 바이러스를 아래와 같이 활성 상태로 변경한 경우 6초면 모든 칸에 바이러스를 퍼뜨릴 수 있다. 
벽은 -, 비활성 바이러스는 *, 활성 바이러스는 0, 빈 칸은 바이러스가 퍼지는 시간으로 표시했다.

* 6 5 4 - - 2
5 6 - 3 - 0 1
4 - - 2 - 1 2
3 - 2 1 2 2 3
2 2 1 0 1 - -
1 - 2 1 2 3 4
0 - 3 2 3 4 *

시간이 최소가 되는 방법은 아래와 같고, 4초만에 모든 칸에 바이러스를 퍼뜨릴 수 있다.
0 1 2 3 - - 2
1 2 - 3 - 0 1
2 - - 2 - 1 2
3 - 2 1 2 2 3
3 2 1 0 1 - -
4 - 2 1 2 3 4
* - 3 2 3 4 *
연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.

입력
첫째 줄에 연구소의 크기 N(4 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.
둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 
0은 빈 칸, 1은 벽, 2는 비활성 바이러스의 위치이다. 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.

출력
연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력한다. 
바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력한다.
"""
import sys
from collections import deque

def bfs():
    global result
    max_num=0
    cnt=0
    q=deque()
    A_visited=[[0 for _ in range(N)] for _ in range(N)]
    for i in range(len(birus)):
        if visited[i]==1:
            A_visited[birus[i][0]][birus[i][1]]=-1
            q.append([birus[i][0],birus[i][1],0])

    while q:
        x,y,d = q.popleft()
        if max_num>=result:
            return
        for i in location:
            n_x=x+i[0]
            n_y=y+i[1]
            if 0<=n_x<N and 0<=n_y<N and A_visited[n_x][n_y]==0 and A[n_x][n_y]!=1:
                if A[n_x][n_y]==0:
                    q.append([n_x,n_y,d+1])
                    A_visited[n_x][n_y]=d+1
                    max_num=max(max_num, d+1)
                    cnt+=1
                else:
                    q.append([n_x,n_y,d+1])
                    A_visited[n_x][n_y]=d+1

    if A_cnt==cnt:
        result=min(result,max_num)

def dfs(v, depth):
    if depth==M:
        bfs()
        return
    for i in range(v,len(birus)):
        if visited[i]==0:
            visited[i]=1
            dfs(i+1, depth+1)
            visited[i]=0

location=[[1,0],[0,1],[-1,0],[0,-1]]
N,M = map(int, sys.stdin.readline().strip().split())
A=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
result=N*N
A_cnt=0
birus=[]
for x in range(N):
    for y in range(N):
        if A[x][y]==0:
            A_cnt+=1
        if A[x][y]==2:
            birus.append([x,y])
visited=[0 for _ in range(len(birus))]
dfs(0,0)
print(-1 if result==N*N else result)