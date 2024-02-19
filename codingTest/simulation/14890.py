# 경사로
"""
크기가 NxN인 지도가 있다. 지도의 각 칸에는 그 곳의 높이가 적혀져 있다.
오늘은 이 지도에서 지나갈 수 있는 길이 몇 개 있는지 알아보려고 한다. 
길이란 한 행 또는 한 열 전부를 나타내며, 한쪽 끝에서 다른쪽 끝까지 지나가는 것이다.
다음과 같은 N=6인 경우 지도를 살펴보자.
이때, 길은 총 2N개가 있으며, 아래와 같다.

길을 지나갈 수 있으려면 길에 속한 모든 칸의 높이가 모두 같아야 한다.
또는, 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다. 경사로는 높이가 항상 1이며, 길이는 L이다.
또, 개수는 매우 많아 부족할 일이 없다. 경사로는 낮은 칸과 높은 칸을 연결하며, 
아래와 같은 조건을 만족해야한다.
경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.
아래와 같은 경우에는 경사로를 놓을 수 없다.

경사로를 놓은 곳에 또 경사로를 놓는 경우
낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
경사로를 놓다가 범위를 벗어나는 경우
L = 2인 경우에 경사로를 놓을 수 있는 경우를 그림으로 나타내면 아래와 같다.

경사로를 놓을 수 없는 경우는 아래와 같다.


위의 그림의 가장 왼쪽부터 1번, 2번, 3번, 4번 예제라고 했을 때, 1번은 높이 차이가 1이 아니라서, 2번은 경사로를 바닥과 접하게 놓지 않아서, 3번은 겹쳐서 놓아서, 4번은 기울이게 놓아서 불가능한 경우이다.
가장 위에 주어진 그림 예의 경우에 지나갈 수 있는 길은 파란색으로, 지나갈 수 없는 길은 빨간색으로 표시되어 있으며, 아래와 같다. 경사로의 길이 L = 2이다.


지도가 주어졌을 때, 지나갈 수 있는 길의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (2 ≤ N ≤ 100)과 L (1 ≤ L ≤ N)이 주어진다. 둘째 줄부터 N개의 줄에 지도가 주어진다. 각 칸의 높이는 10보다 작거나 같은 자연수이다.

출력
첫째 줄에 지나갈 수 있는 길의 개수를 출력한다.

풀이
cnt=0

가로 검사
* 왼쪽에서 오른쪽으로 이동하면서 검사
  * 나 다음의 크기가 같다면 pass
  * 나 다음 크기가 2이상 -2 이하라면 break
  * 나 다음의 크기가 1 차이가 난다면
    * 현재 위치가 왼쪽으로 부터 L 이상차이가 나는지 확인
    * 경사로를 놓을 곳에 경사로가 있는지 확인
  * 나 다음의 크기가 -1 차이가 난다면
    * 현재 위치가 오른쪽으로 부터 L 이상차이가 나는지 확인
    * 경사로를 놓을 곳에 경사로가 있는지 확인

세로 검사도 위와 비슷
"""
import sys

# 그리드의 크기(N)와 도로 세그먼트의 최소 길이(L)를 읽음
N, L = map(int, sys.stdin.readline().strip().split())

# 도로 행렬을 읽음
road = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# 사용된 도로 세그먼트를 추적하기 위한 행렬 초기화
road_exist = [[0 for _ in range(N)] for _ in range(N)]  # 행에 대한 행렬
road_exist_1 = [[0 for _ in range(N)] for _ in range(N)]  # 열에 대한 행렬

# 유효한 도로의 수를 세기 위한 카운터 초기화
cnt = 0

# 도로 세그먼트가 특정 조건을 만족하는지 확인하는 함수 (행에 대한 함수)
def chk(n, i, min, max):
   tmp = road[n][i]
   for k in range(min, max):
      if tmp != road[n][k] or road_exist[n][k] != 0:
         return False
   for k in range(min, max):
      road_exist[n][k] = 1
   return True

# 각 행에 대해 반복
for n in range(N):
   for i in range(N):
      if i == N-1:
         cnt += 1
         break
      if road[n][i] == road[n][i+1]:
         continue
      if road[n][i] - road[n][i+1] > 1 or road[n][i] - road[n][i+1] < -1:
         break
      else:
         if road[n][i] - road[n][i+1] == -1:
            if i >= (L-1):
               if not chk(n, i, i-(L-1), i+1):
                  break
            else:
               break
            continue
         elif road[n][i] - road[n][i+1] == 1:
            if N-1-i >= L:
               if not chk(n, i+1, i+1, i+L+1):
                  break
            else:
               break
            continue

# 도로 세그먼트가 특정 조건을 만족하는지 확인하는 함수 (열에 대한 함수)
def chk_1(n, i, min, max):
   tmp = road[i][n]
   for k in range(min, max):
      if tmp != road[k][n] or road_exist_1[k][n] != 0:
         return False
   for k in range(min, max):
      road_exist_1[k][n] = 1
   return True

# 각 열에 대해 반복
for n in range(N):
   for i in range(N):
      if i == N-1:
         cnt += 1
         break
      if road[i][n] == road[i+1][n]:
         continue
      if road[i][n] - road[i+1][n] > 1 or road[i][n] - road[i+1][n] < -1:
         break
      else:
         if road[i][n] - road[i+1][n] == -1:
            if i >= (L-1):
               if not chk_1(n, i, i-(L-1), i+1):
                  break
            else:
               break
            continue
         elif road[i][n] - road[i+1][n] == 1:
            if N-1-i >= L:
               if not chk_1(n, i+1, i+1, i+L+1):
                  break
            else:
               break
            continue

# 최종적으로 세어진 유효한 도로의 수를 출력
print(cnt)