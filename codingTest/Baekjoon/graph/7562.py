#나이트의 이동
"""
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다
나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇번 움직이면 이 칸으로 이동할 수 있을까?

입력
입력의 첫째 줄에는 테스트케이스의 개수가 주어진다
각 테스트 케이스는 세 줄로 이루어져 있다. 
첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 
체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 
둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

1
8
0 0
7 0
"""
import sys
from collections import deque

distance =[[-2,-1],[-2,1],[-1,2],[-1,-2],[1,-2],[1,2],[2,-1],[2,1]]

def bfs():
    if s_x==b_x and s_y==b_y:
        return 0
    queue = deque()
    queue.append([s_x,s_y])

    while queue:
        n_x, n_y = queue.popleft()
        for i in distance:
            x=n_x+i[0]
            y=n_y+i[1]
            if 0<=x<l and 0<=y<l and map_list[x][y]==0:
                queue.append([x,y])
                map_list[x][y]=map_list[n_x][n_y]+1
            if x==b_x and y==b_y:
                return map_list[x][y]

for _ in range(int(sys.stdin.readline().strip())):
    l=int(sys.stdin.readline())
    s_x, s_y = map(int, sys.stdin.readline().strip().split())
    b_x, b_y = map(int, sys.stdin.readline().strip().split())
    map_list=[[0 for _ in range(l)] for _ in range(l)]
    print(bfs())