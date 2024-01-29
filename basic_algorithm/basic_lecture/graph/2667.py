#단지 번호 붙이기
"""
시간제한 1초
메모리제한 128MB

<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. 
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고
그 다음 N줄에는 각각 N개의 자료(0 혹은 1)가 입력된다

출력
첫번째 줄에는 총 단지 수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한줄에 하나씩 출력하시오

나의 풀이
내가 탐색할 수 있는 부분은 1이면서 방문하지 않은 곳이다
그래서 모든 곳을 확인하면 탐색할 수 있는 곳을 찾고그 곳에서 탐색을 시작하고 탐색이 끝나면 단지+1이 되는 것이다
움직임은 상하죄우로만 움직인다

정리할 내용 까먹을까봐 기록
입력
"""
import sys
from collections import deque

location=[[0,1], [0,-1], [1,0],[-1,0]]

def bfs(x,y):
    visited[x][y]=1
    queue = deque()
    queue.append([x,y])
    count=1

    while queue:
        now_x, now_y = queue.popleft()
        for before in location:
            if 0<=now_x+before[0]<N and 0<=now_y+before[1]<N and visited[now_x+before[0]][now_y+before[1]]==0 and N_list[now_x+before[0]][now_y+before[1]]==1:
                count+=1
                queue.append([now_x+before[0],now_y+before[1]])
                visited[now_x+before[0]][now_y+before[1]]=1
    return count

N= int(sys.stdin.readline())
N_list = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

visited=[[0 for _ in range(N)] for _ in range(N)]

count=0
result=[]
for x in range(N):
    for y in range(N):
        if visited[x][y]==0 and N_list[x][y]==1:
            result.append(bfs(x,y))
            count+=1
print(count)
for i in sorted(result):
    print(i)