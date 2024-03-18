#미세먼지 안녕!
"""
시간제한 1초
메모리 제한 512MB

미세먼지를 제거하기 위해 구사과는 공기청정기를 설치하려고 한다. 
공기청정기의 성능을 테스트하기 위해 구사과는 집을 크기가 RxC인 격자판으로 나타냈고, 1x1 크기의 칸으로 나눴다. 
구사과는 뛰어난 코딩 실력을 이용해 각 칸 (r, c)에 있는 미세먼지의 양을 실시간으로 모니터링하는 시스템을 개발했다. (r, c)는 r행 c열을 의미한다.

공기청정기는 항상 1번 열에 설치되어 있고, 크기는 두 행을 차지한다. 공기청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, (r, c)에 있는 미세먼지의 양은 Ar,c이다.

1초 동안 아래 적힌 일이 순서대로 일어난다.

1. 미세먼지가 확산된다. 
  * 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
  * (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
  * 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
  * 확산되는 양은 Ar,c/5이고 소수점은 버린다. 즉, ⌊Ar,c/5⌋이다.
  * (r, c)에 남은 미세먼지의 양은 Ar,c - ⌊Ar,c/5⌋x(확산된 방향의 개수) 이다.
2. 공기청정기가 작동한다.
  * 공기청정기에서는 바람이 나온다.
  * 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
  * 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
  * 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

방의 정보가 주어졌을 때, T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양을 구해보자.

입력
첫째 줄에 R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 가 주어진다.

둘째 줄부터 R개의 줄에 Ar,c (-1 ≤ Ar,c ≤ 1,000)가 주어진다. 
공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다. -1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.

출력
첫째 줄에 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.
"""
import sys

# 공기청정기 위치 체크
def chk():
    for x in range(R):
        for y in range(C):
            if A[x][y] == -1:
                T_list.append([x, y])

# 미세먼지 확산
def spread():
    global A
    result = [[0 for _ in range(C)] for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if A[x][y] != 0 and A[x][y] != -1:
                cnt = 0
                for i in loc:
                    n_x = x + i[0]
                    n_y = y + i[1]
                    if 0 <= n_x < R and 0 <= n_y < C and [n_x, n_y] not in T_list:
                        cnt += 1
                        result[n_x][n_y] += A[x][y] // 5
                result[x][y] += A[x][y] - (A[x][y] // 5) * cnt

    A = result[:]

# 공기청정기 작동 - 위쪽 공기청정기
def up_move(X, Y):
    # 오른쪽으로
    tmp = A[X][Y]
    for y in range(Y, C - 1):
        tmp1 = A[X][y + 1]
        A[X][y + 1] = tmp
        tmp = tmp1
    # 위로
    for x in range(X, 0, -1):
        tmp1 = A[x - 1][C - 1]
        A[x - 1][C - 1] = tmp
        tmp = tmp1
    # 왼쪽으로
    for y in range(C - 1, 0, -1):
        tmp1 = A[0][y - 1]
        A[0][y - 1] = tmp
        tmp = tmp1
    # 아래로
    for x in range(0, X):
        tmp1 = A[x + 1][0]
        A[x + 1][0] = tmp
        tmp = tmp1

    A[X][Y] = 0

# 공기청정기 작동 - 아래쪽 공기청정기
def down_move(X, Y):
    # 오른쪽으로
    tmp = A[X][Y]
    for y in range(Y, C - 1):
        tmp1 = A[X][y + 1]
        A[X][y + 1] = tmp
        tmp = tmp1
    # 아래로
    for x in range(X, R - 1):
        tmp1 = A[x + 1][C - 1]
        A[x + 1][C - 1] = tmp
        tmp = tmp1
    # 왼쪽으로
    for y in range(C - 1, 0, -1):
        tmp1 = A[R - 1][y - 1]
        A[R - 1][y - 1] = tmp
        tmp = tmp1
    # 위로
    for x in range(R - 1, X, -1):
        tmp1 = A[x - 1][0]
        A[x - 1][0] = tmp
        tmp = tmp1

    A[X][Y] = 0

# 입력 받기
R, C, T = map(int, sys.stdin.readline().strip().split())
A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(R)]
loc = [[0, 1], [1, 0], [-1, 0], [0, -1]]
T_list = []
chk()

# T만큼 반복하면서 확산과 공기청정기 작동 실행
for _ in range(T):
    spread()
    up_move(T_list[0][0], T_list[0][1])
    down_move(T_list[1][0], T_list[1][1])

# 결과 출력
print(sum([sum(i) for i in A]))
