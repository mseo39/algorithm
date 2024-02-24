#배열 복원하기
"""
시간제한 2초
메모리제한 512MB

크기가 H x W인 배열 A와 두 정수 X와 Y가 있을 때, 
크기가 (H + X) x (W + Y)인 배열 B는 배열 A와 배열 A를 아래로 X칸, 오른쪽으로 Y칸 이동시킨 배열을 겹쳐 만들 수 있다. 
수가 겹쳐지면 수가 합쳐진다.

즉, 배열 B의 (i, j)에 들어있는 값은 아래 3개 중 하나이다.
(i, j)가 두 배열 모두에 포함되지 않으면, Bi,j = 0이다.
(i, j)가 두 배열 모두에 포함되면, Bi,j = Ai,j + Ai-X,j-Y이다.
(i, j)가 두 배열 중 하나에 포함되면, Bi,j = Ai,j 또는 Ai-X,j-Y이다.
배열 B와 정수 X, Y가 주어졌을 때, 배열 A를 구해보자.

입력
첫째 줄에 네 정수 H, W, X, Y가 주어진다. 둘째 줄부터 H + X개의 줄에 배열 B의 원소가 주어진다.
항상 배열 A가 존재하는 경우만 입력으로 주어진다.

출력
총 H개의 줄에 배열 A의 원소를 출력한다.

2 3 0 1
1 2 2 1
1 2 2 1
"""

import sys
H,W,X,Y = map(int, sys.stdin.readline().strip().split())
map_list=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(H+X)]
result=[map_list[i][:W] for i in range(H)]

for h in range(X,H):
    for w in range(Y,W):
        result[h][w]=result[h][w]-map_list[h-X][w-Y]
        map_list[h][w]=result[h][w]

for i in result:
    print(*i)


"""import sys
H,W,X,Y = map(int, sys.stdin.readline().strip().split())
map_list=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(H+X)]
result=[[0 for _ in range(W)] for _ in range(H)]

for h in range(X):
    result[h]=map_list[h][:W]

for w in range(Y):
    for h in range(H):
        result[h][w]=map_list[h][w]

result[H-1]=map_list[H+X-1][Y:W+Y]

for h in range(X,H-X):
    for w in range(Y,W):
        result[h][w]=map_list[h][w]-result[h-1][w-1]


for i in result:
    print(*i)"""