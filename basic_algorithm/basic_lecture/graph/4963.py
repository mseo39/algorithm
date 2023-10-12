#섬의 개수
"""
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 
두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 
각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. 
w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
"""
from collections import deque

"""
상 -1 0
하 1 0
좌 0 -1
우 0 1
대각선 -1-1, -1 1, 1 -1, 1 1
"""
direct= [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]

while(True):
    w,h = map(int, input().split())
    #0 0이 입력되면 입력을 멈춘다
    if w==0 and h==0:
        break
    #1은 땅, 0은 바다
    tmp=[list(map(int, input().split())) for _ in range(h)]
    chk=[[0 for _ in range(w)] for _ in range(h)]

    num=0
    #dfs
    for x in range(h):
        for y in range(w):
            if tmp[x][y]==1 and chk[x][y]==0:
                queue=deque([[x,y]])
                chk[x][y]=1

                while queue:
                    now= queue.popleft()

                    for i in direct:
                        dx=now[0]+i[0]
                        dy=now[1]+i[1]
                        if 0<= dx < h and 0<= dy < w:
                            if tmp[dx][dy]==1 and chk[dx][dy]==0:
                                queue.append([dx,dy])
                                chk[dx][dy]=1
                num+=1
    print(num)