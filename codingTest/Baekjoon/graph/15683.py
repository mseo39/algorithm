#감시
"""
스타트링크의 사무실은 1x1크기의 정사각형으로 나누어져 있는 NxM 크기의 직사각형으로 나타낼 수 있다. 
사무실에는 총 K개의 CCTV가 설치되어져 있는데, CCTV는 5가지 종류가 있다. 각 CCTV가 감시할 수 있는 방법은 다음과 같다.
1번 CCTV는 한 쪽 방향만 감시할 수 있다. 2번과 3번은 두 방향을 감시할 수 있는데, 2번은 감시하는 방향이 서로 반대방향이어야 하고, 
3번은 직각 방향이어야 한다. 4번은 세 방향, 5번은 네 방향을 감시할 수 있다.

CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다. 사무실에는 벽이 있는데, CCTV는 벽을 통과할 수 없다. CCTV가 감시할 수 없는 영역은 사각지대라고 한다.
CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향으로 해야 하며, 감시하려고 하는 방향이 가로 또는 세로 방향이어야 한다.
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
지도에서 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호이다. 위의 예시에서 1번의 방향에 따라 감시할 수 있는 영역을 '#'로 나타내면 아래와 같다.

->
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 # 6 0
0 0 0 0 0 0
<-
0 0 0 0 0 0
0 0 0 0 0 0
# # 1 0 6 0
0  0 0 0 0 0
↑
0 0 # 0 0 0
0 0 # 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
↓
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 # 0 0 0
CCTV는 벽을 통과할 수 없기 때문에, 1번이 → 방향을 감시하고 있을 때는 6의 오른쪽에 있는 칸을 감시할 수 없다.


0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5
위의 예시에서 감시할 수 있는 방향을 알아보면 아래와 같다.

왼쪽 상단 2: ↔, 오른쪽 하단 2: ↔
0 0 0 0 0 #
# 2 # # # #
0 0 0 0 6 #
0 6 # # 2 #
0 0 0 0 0 #
# # # # # 5
왼쪽 상단 2: ↔, 오른쪽 하단 2: ↕
0 0 0 0 0 #
# 2 # # # #
0 0 0 0 6 #
0 6 0 0 2 #
0 0 0 0 # #
# # # # # 5
왼쪽 상단 2: ↕, 오른쪽 하단 2: ↔
0 # 0 0 0 #
0 2 0 0 0 #
0 # 0 0 6 #
0 6 # # 2 #
0 0 0 0 0 #
# # # # # 5
왼쪽 상단 2: ↕, 오른쪽 하단 2: ↕
0 # 0 0 0 #
0 2 0 0 0 #
0 # 0 0 6 #
0 6 0 0 2 #
0 0 0 0 # #
# # # # # 5


CCTV는 CCTV를 통과할 수 있다. 아래 예시를 보자.

0 0 2 0 3
0 6 0 0 0
0 0 6 6 0
0 0 0 0 0
위와 같은 경우에 2의 방향이 ↕ 3의 방향이 ←와 ↓인 경우 감시받는 영역은 다음과 같다.
# # 2 # 3
0 6 # 0 #
0 0 6 6 #
0 0 0 0 #

사무실의 크기와 상태, 그리고 CCTV의 정보가 주어졌을 때, CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다. 

CCTV의 최대 개수는 8개를 넘지 않는다.

출력
첫째 줄에 사각 지대의 최소 크기를 출력한다.
"""
import sys
up=[-1,0]
down=[1,0]
left=[0,-1]
right=[0,1]
D=[[[right], [down], [left],[up]],
   [[left,right],[up,down]],
   [[up,right],[right,down],[left,down],[left,up]],
   [[left,up,right],[up,right,down],[right,down,left],[up,left,down]],
   [[left,right,up,down]]
   ]

def chk():
    global max_num
    cnt=0
    visited=[[0 for _ in range(M)] for _ in range(N)]
    for i in cctv:
        x=i[0][0]
        y=i[0][1]
        for d in D[K[x][y]-1][i[1]]:
            tmpX=x
            tmpY=y
            while(0<=tmpX<N and 0<=tmpY<M):
                if K[tmpX][tmpY]==6:
                    break
                if K[tmpX][tmpY]==0 and visited[tmpX][tmpY]==0:
                    cnt+=1
                    visited[tmpX][tmpY]="#"
                tmpX+=d[0]
                tmpY+=d[1]
    max_num=max(max_num,cnt)

def dfs(v):
    if v==len(cctv):
        chk()
        return
    for i in range(len(D[K[cctv[v][0][0]][cctv[v][0][1]]-1])):
        cctv[v][1]=i
        dfs(v+1)

N, M = map(int, sys.stdin.readline().strip().split())
K= [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]
max_num=-1
cctv=[]
room=N*M
for x in range(N):
    for y in range(M):
        if K[x][y]!=0 and K[x][y]!=6:
            cctv.append([[x,y],0])
        if K[x][y]!=0:
            room-=1
dfs(0)
print(room-max_num)