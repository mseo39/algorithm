#알고스팟
"""
시간제한 1초
메모리제한 128MB

알고스팟 운영진이 모두 미로에 갇혔다. 미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다. 
미로는 빈 방 또는 벽으로 이루어져 있고, 
빈 방은 자유롭게 다닐 수 있지만, 
벽은 부수지 않으면 이동할 수 없다.

알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다. 즉, 여러 명이 다른 방에 있을 수는 없다. 
어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다. 
즉, 현재 운영진이 (x, y)에 있을 때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다. 
단, 미로의 밖으로 이동 할 수는 없다.

벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다. 벽을 부수면, 빈 방과 동일한 방으로 변한다.

만약 이 문제가 알고스팟에 있다면, 운영진들은 궁극의 무기 sudo를 이용해 벽을 한 번에 다 없애버릴 수 있지만, 
안타깝게도 이 문제는 Baekjoon Online Judge에 수록되어 있기 때문에, sudo를 사용할 수 없다.

현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 미로의 크기를 나타내는 가로 크기 M, 세로 크기 N(1 ≤ N, M ≤ 100)이 주어진다.
다음 N개의 줄에는 미로의 상태를 나타내는 숫자 0과 1이 주어진다 0은 빈 방을 의미하고 1은 벽을 의미한다
(1,1)과 (N,M)은 항상 뚫려있다

출력
첫째 줄에 알고스팟 운영진이 (N,M)으로 이동하기 위해 벽을 최소 몇개를 부수어야 하는지 출력한다

문제 정리
방은 2가지 - 빈방(0), 벽(1) -> 빈방으로만 이동할 수 있다
이동 가능한 방향 - 상하좌우 (x+1, y), (x, y+1), (x-1, y), (x, y-1)
"""

import sys
from collections import deque

location=[[1,0],[0,1],[-1,0],[0,-1]]

def bfs():
    if N==1 and M==1:
        return 0
    queue = deque()
    queue.append([0,0,0])
    visited[0][0]=1

    while queue:
        n_x, n_y,n=queue.popleft()
        for i in location:
            b_x=n_x+i[0]
            b_y=n_y+i[1]
            if b_x==N-1 and b_y==M-1:
                return n
            if 0<=b_x<N and 0<=b_y<M and visited[b_x][b_y]==0:
                visited[b_x][b_y]=1
                
                if map_list[b_x][b_y]==0:
                    queue.appendleft([b_x,b_y,n])
                else:
                    queue.append([b_x,b_y,n+1])


M, N = map(int, sys.stdin.readline().strip().split())
map_list = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited=[[0 for _ in range(M)] for _ in range(N)]
print(bfs())

"""import sys
from collections import deque

location=[[1,0],[0,1],[-1,0],[0,-1]]

def bfs():
    global min_num
    if N==1 and M==1:
        min_num=0
        return
    queue = deque()
    queue.append([0,0,0])
    visited[0][0]=1

    while queue:
        n_x, n_y,n=queue.popleft()
        if n>=min_num:
            continue
        for i in location:
            b_x=n_x+i[0]
            b_y=n_y+i[1]
            if b_x==N-1 and b_y==M-1:
                min_num=min(min_num,n)
                continue
            if 0<=b_x<N and 0<=b_y<M and visited[b_x][b_y]==0:
                visited[b_x][b_y]=1
                
                if map_list[b_x][b_y]==0:
                    queue.appendleft([b_x,b_y,n])
                else:
                    queue.append([b_x,b_y,n+1])


M, N = map(int, sys.stdin.readline().strip().split())
map_list = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited=[[0 for _ in range(M)] for _ in range(N)]
min_num=N*M+1
bfs()
print(min_num)"""