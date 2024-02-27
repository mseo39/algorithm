#연결 요소의 개수
"""
시간제한 3초
메모리제한 512MB

방향 없는 그래프가 주어졌을 때,, 연결 요소의 개수를 구하는 프로그램을 작성하시오

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ Nx(N-1)/2) 
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다
"""

import sys
from collections import deque

def bfs(v):
    queue=deque()
    queue.append(v)

    while queue:
        now=queue.popleft()
        for i in M_list[now]:
            if arr[i]==0:
                queue.append(i)
                arr[i]=1

N,M = map(int, sys.stdin.readline().strip().split())
M_list = [[] for _ in range(N)]
arr=[0 for _ in range(N)]
count=0

for _ in range(M):
    tmp = list(map(int, sys.stdin.readline().strip().split()))
    M_list[tmp[0]-1].append(tmp[1]-1)
    M_list[tmp[1]-1].append(tmp[0]-1)

for i in range(N):
    if not arr[i]:
        if not M_list[i]:
            arr[i]=1
            count+=1
        else:
            bfs(i)
            count+=1
print(count)

"""import sys
sys.setrecursionlimit(10**7)

def solution(start, dept):
    arr[start]=1
    for i in M_list[start]:
        if arr[i]==0:
            solution(i,dept+1)

N,M = map(int, sys.stdin.readline().strip().split())
M_list = [[] for _ in range(N)]
arr=[0 for _ in range(N)]
count=0

for _ in range(M):
    tmp = list(map(int, sys.stdin.readline().strip().split()))
    M_list[tmp[0]-1].append(tmp[1]-1)
    M_list[tmp[1]-1].append(tmp[0]-1)

for i in range(N):
    if not arr[i]:
        if not M_list[i]:
            arr[i]=1
            count+=1
        else:
            solution(i, 0)
            count+=1
print(count)"""