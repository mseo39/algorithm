#미로 탐색
"""
시간제한 1초
메모리 제한 192MB

NxM크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, 
(1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
"""
import sys
from collections import deque

location = [[0,-1],[0,1],[1,0],[-1,0]]

def bfs(x,y):
    global min_num
    visited[x][y]=1
    queue = deque()
    queue.append([x,y,1])

    while queue:
        n_x, n_y, n_d = queue.popleft()
        for i in location:
            b_x=i[0]+n_x
            b_y=i[1]+n_y
            if b_x==N-1 and b_y==M-1:
                return n_d+1
            if 0<=b_x<N and 0<=b_y<M and map_list[b_x][b_y]==1 and visited[b_x][b_y]==0:
                queue.append([b_x, b_y,n_d+1])
                visited[b_x][b_y]=1

N, M = map(int, sys.stdin.readline().strip().split())
map_list=[list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited=[[0 for _ in range(M)] for _ in range(N)]
print(bfs(0,0))