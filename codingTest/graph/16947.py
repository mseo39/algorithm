#서울 지하철 2호선
"""
시간제한 2초
메모리제한 512MB

서울 지하철 2호선은 다음과 같이 생겼다
지하철 2호선에는 51개의 역이 있고, 역과 역 사이를 연결하는 구간이 51개 있다. 
즉, 정점이 51개이고, 양방향 간선이 51개인 그래프로 나타낼 수 있다. 2호선은 순환선 1개와 2개의 지선으로 이루어져 있다. 
한 역에서 출발해서 계속 가면 다시 출발한 역으로 돌아올 수 있는 노선을 순환선이라고 한다. 
지선은 순환선에 속하는 한 역에서 시작하는 트리 형태의 노선이다.

두 역(정점) 사이의 거리는 지나야 하는 구간(간선)의 개수이다. 
역 A와 순환선 사이의 거리는 A와 순환선에 속하는 역 사이의 거리 중 최솟값이다.

지하철 2호선과 같은 형태의 노선도가 주어졌을 때, 각 역과 순환선 사이의 거리를 구해보자.

입력
첫째 줄에 역의 개수 N(3 ≤ N ≤ 3,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 역과 역을 연결하는 구간의 정보가 주어진다. 
같은 구간이 여러 번 주어지는 경우는 없고, 역은 1번부터 N번까지 번호가 매겨져 있다. 
임의의 두 역 사이에 경로가 항상 존재하는 노선만 입력으로 주어진다.

출력
총 N개의 정수를 출력한다. 
1번 역과 순환선 사이의 거리, 2번 역과 순환선 사이의 거리, ..., N번 역과 순환선 사이의 거리를 공백으로 구분해 출력한다.

기억해야 할 것
깊이 사용

"""
import sys
from collections import deque
sys.setrecursionlimit(100000)

def dfs(v, dept):

    for i in N_list[v]:
        if arr[0]==i and dept>1:
            return True
        if i not in arr:
            arr.append(i)
            if dfs(i,dept+1):
                return True
            arr.pop()

def bfs():
    chk=[-1 for _ in range(N+1)]
    queue = deque()

    for i in arr:
        queue.append(i)
        chk[i]=0

    while queue:
        n = queue.popleft()
        for i in N_list[n]:
            if chk[i]==-1:
                queue.append(i)
                chk[i]=chk[n]+1
    print(*chk[1:])



N= int(sys.stdin.readline())
N_list =[[] for _ in range(N+1)]
for _ in range(N):
    x,y=map(int, sys.stdin.readline().strip().split())
    N_list[x].append(y)
    N_list[y].append(x)

arr=[]

for i in range(1,N+1):
    arr.append(i)
    if dfs(i,0):
        break
    arr.pop()

bfs()