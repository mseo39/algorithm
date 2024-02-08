#유기농 배추
"""
차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 
농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 
한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 
특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 
그 배추들 역시 해충으로부터 보호받을 수 있다. 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.
한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다. 
배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다. 
예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다. 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.

1	1	0	0	0	0	0	0	0	0
0	1	0	0	0	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	1	1	0	0	0	1	1	1
0	0	0	0	1	0	0	1	1	1

입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 
그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 
그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 
두 배추의 위치가 같은 경우는 없다.

출력
각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

x y
상 x-1,y
하 x+1, y
왼 x, y-1
오 x, y+1

다음과 같이 했을 때 시간이 너무 오래 걸린다 그래서 생각해보니 굳이 이중for문을 돌리지 않아도 된다는걸 깨달았다
이미 위치를 다 알고 있으니깐 그것만 알면 되겠구나..?

from collections import deque

direction =[[-1,0],[1,0],[0,-1],[0,1]]


#테스트케이스 입력
T=int(input())
#가로길이 M, 세로길이 N, 배추가 심어져있는 개수 K
for _ in range(T):
    M,N,K=map(int, input().split())
    tmp=[[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x,y=map(int, input().split())
        tmp[y][x]=1
    
    #dfs
    cnt=0
    for x in range(N):
        for y in range(M):
            if tmp[x][y]==1:
                queue = deque([[x,y]])
                while queue:
                    now= queue.popleft()

                    for i in direction:
                        dx=now[0]+i[0]
                        dy=now[1]+i[1]

                        if 0<= dx <N and 0<= dy <M:
                            if tmp[dx][dy]:
                                queue.append([dx,dy])
                cnt+=1
    print(cnt)
"""
from collections import deque

# 상, 하, 좌, 우로 이동하는 방향을 표현하는 리스트
direction =[[-1,0],[1,0],[0,-1],[0,1]]


#테스트케이스 입력
T=int(input())
#가로길이 M, 세로길이 N, 배추가 심어져있는 개수 K
for _ in range(T):
    M,N,K=map(int, input().split())
    # 각 배추의 위치를 입력받아 리스트로 저장합니다.
    tmp=[list(map(int, input().split())) for _ in range(K)]
    # 각 배추의 방문 여부를 나타내는 리스트를 초기화합니다.
    chk=[0 for _ in range(K)]
    
    #dfs

    # 벌레의 개수를 세는 변수를 초기화합니다.
    cnt=0
    # 각 배추 위치에 대해 처리합니다.
    for i in range(len(tmp)):
        # 만약 이미 방문한 배추라면 다음 배추로 넘어갑니다.
        if chk[i]==1:
            continue
        # BFS를 위한 큐를 초기화하고 현재 배추 위치를 큐에 넣습니다.
        queue = deque([[tmp[i][0],tmp[i][1]]])
        while queue:
            # 큐에서 현재 위치를 꺼냅니다.
            now= queue.popleft()
            # 상, 하, 좌, 우 방향으로 이동하며 인접한 배추를 찾습니다.
            for d in direction:
                dx=now[0]+d[0]
                dy=now[1]+d[1]
                # 만약 이동한 위치에 배추가 있고, 아직 방문하지 않았다면 큐에 추가하고 방문 표시를 합니다.
                if [dx,dy] in tmp and chk[tmp.index([dx,dy])]==0:
                    queue.append([dx,dy])
                    chk[tmp.index([dx,dy])]=1
        # 한 영역의 배추를 모두 방문한 경우 벌레 개수를 1 증가시킵니다
        cnt+=1
    # 현재 테스트 케이스에서 발견한 벌레의 개수를 출력합니다.
    print(cnt)