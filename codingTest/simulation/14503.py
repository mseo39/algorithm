# 로봇 청소기
"""
로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 방은 NXM 크기의 직사각형으로 나타낼 수 있으며, 1X1 크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 
청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북 중 하나이다. 
방의 각 칸은 좌표 (r, c)로 나타낼 수 있고, 
가장 북쪽 줄의 가장 서쪽 칸의 좌표가 (0, 0), 
가장 남쪽 줄의 가장 동쪽 칸의 좌표가 (N-1, M-1)이다. 
즉, 좌표 (r, c)는 북쪽에서 (r+1)번째에 있는 줄의 서쪽에서 (c+1)번째 칸을 가리킨다. 
처음에 빈 칸은 전부 청소되지 않은 상태이다.

로봇 청소기는 다음과 같이 작동한다.

1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
  1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
  2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
  1. 반시계 방향으로 90도 회전한다.
  2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
  3. 1번으로 돌아간다.

입력
첫째 줄에 방의 크기 N과 M이 입력된다. (3 <= N, M <= 50) 
둘째 줄에 처음에 로봇 청소기가 있는 칸의 좌표 (r, c)와 처음에 로봇 청소기가 바라보는 방향 d가 입력된다. 
d가 
0인 경우 북쪽, 
1인 경우 동쪽, 
2인 경우 남쪽, 
3인 경우 서쪽을 바라보고 있는 것이다.

셋째 줄부터 N개의 줄에 각 장소의 상태를 나타내는 N X M개의 값이 한 줄에 M개씩 입력된다. 
i번째 줄의 j번째 값은 칸 (i, j)의 상태를 나타내며, 
이 값이 0인 경우 (i, j)가 청소되지 않은 빈 칸이고, 
1인 경우 (i, j)에 벽이 있는 것이다. 
방의 가장 북쪽, 가장 남쪽, 가장 서쪽, 가장 동쪽 줄 중 하나 이상에 위치한 모든 칸에는 벽이 있다. 로봇 청소기가 있는 칸은 항상 빈 칸이다.

출력
로봇 청소기가 작동을 시작한 후 작동을 멈출 때까지 청소하는 칸의 개수를 출력한다.

나의 풀이
  북
서  동
  남

"""
import sys

N,M = map(int, sys.stdin.readline().strip().split())
r,c,d = map(int, sys.stdin.readline().strip().split())
room = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)]

move = [[-1,0],[0,1],[1,0],[0,-1]]
location = [[3,2,1,0],[0,3,2,1],[1,0,3,2],[2,1,0,3]]
back = [2,3,0,1]
"""
나는 방향을 위처럼 지정해줬는데 
다른 사람들은 d = (d+3) % 4 이렇게 계산해줬음
"""
cnt=1
room[r][c]=2

def chk():
    """
    현재 칸의 주변 4칸에 청소할 빈킨이 있는지 검사
    있으면 해당 방향으로 업데이트하고 해당 좌표를 반환
    없으면 false를 반환
    """
    global d
    for m in location[d]:
        b_x=r+move[m][0]
        b_y=c+move[m][1]
        if 0<=b_x<N and 0<=b_y<M and room[b_x][b_y]==0:
            d=m
            return [b_x,b_y]
    return False


while(True):
    """
    청소할 곳이 있다면
      좌표를 변경해주고 청소했다고 표시 및 개수 증가
    청소할 곳이 없다면 뒤로 이동
    """
    tmp=chk()
    if not tmp:
        x,y = move[back[d]]
        if room[r+x][c+y]==1:
            break
        else:
            r+=x
            c+=y
    else:
        r=tmp[0]
        c=tmp[1]
        cnt+=1
        room[r][c]=2

print(cnt)