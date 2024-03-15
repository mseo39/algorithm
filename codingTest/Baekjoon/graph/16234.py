#인구이동
"""
시간제한 2초
메모리제한 512MB

NxN크기의 땅이 있고, 땅은 1x1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 
인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1x1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.

오늘부터 인구 이동이 시작되는 날이다.
인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

* 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
* 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
* 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
* 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
* 연합을 해체하고, 모든 국경선을 닫는다.

각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)
둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)
인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.

출력
인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.
"""
import sys
from collections import deque

location = [[1,0],[0,1],[-1,0],[0,-1]]

def bfs(x,y,visited):
    arr=[[x,y]]
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    while q:
        n=q.popleft()
        for l in location:
            n_x=n[0]+l[0]
            n_y=n[1]+l[1]
            if 0<=n_x<N and 0<=n_y<N and L<=abs(A[n_x][n_y]-A[n[0]][n[1]])<=R and visited[n_x][n_y]==0:
                q.append([n_x,n_y])
                arr.append([n_x,n_y])
                visited[n_x][n_y]=1
    if len(arr)==1:
        return False
    
    v=sum(A[a][b] for a,b in arr)//len(arr)
    for i in arr:
        A[i[0]][i[1]]=v
    return True
    
N,L,R = map(int, sys.stdin.readline().strip().split())
A=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

day=0
while(True):
    visited=[[0 for _ in range(N)] for _ in range(N)]
    cnt=0
    for x in range(N):
        for y in range(N):
            #visited[x][y]==0이 없어서 틀린거였음
            if visited[x][y]==0 and not bfs(x,y,visited):
                cnt+=1
        
    if cnt==N*N:
        break
    day+=1

print(day)