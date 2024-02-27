# Two Dots
"""
시간제한 2초
메모리제한 512MB

Two Dots는 Playdots, Inc.에서 만든 게임이다. 게임의 기초 단계는 크기가 NxM인 게임판 위에서 진행된다.

각각의 칸은 색이 칠해진 공이 하나씩 있다. 이 게임의 핵심은 같은 색으로 이루어진 사이클을 찾는 것이다.

다음은 위의 게임판에서 만들 수 있는 사이클의 예시이다.

점 k개 d1, d2, ..., dk로 이루어진 사이클의 정의는 아래와 같다.

모든 k개의 점은 서로 다르다. 
k는 4보다 크거나 같다.
모든 점의 색은 같다.
모든 1 ≤ i ≤ k-1에 대해서, di와 di+1은 인접하다. 또, dk와 d1도 인접해야 한다. 
두 점이 인접하다는 것은 각각의 점이 들어있는 칸이 변을 공유한다는 의미이다.
게임판의 상태가 주어졌을 때, 사이클이 존재하는지 아닌지 구해보자.

입력
첫째 줄에 게임판의 크기 N, M이 주어진다. 
둘째 줄부터 N개의 줄에 게임판의 상태가 주어진다. 게임판은 모두 점으로 가득차 있고, 
게임판의 상태는 점의 색을 의미한다. 점의 색은 알파벳 대문자 한 글자이다.

출력
사이클이 존재하는 경우에는 "Yes", 없는 경우에는 "No"를 출력한다.
"""
import sys
location =[[1,0], [0,1], [-1,0], [0,-1]]

def dfs(x,y,v):
    for i in location:
        b_x=x+i[0]
        b_y=y+i[1]
        if 0<=b_x<N and 0<=b_y<M and map_list[b_x][b_y]==v:
            if len(arr)>=4 and arr[0][0]==b_x and arr[0][1]==b_y:
                return True
            if [b_x,b_y] not in arr:
                arr.append([b_x,b_y])
                if dfs(b_x,b_y,v):
                    return True
                arr.pop()
    return False


N, M = map(int, sys.stdin.readline().strip().split())
map_list= [sys.stdin.readline().strip() for _ in range(N)]
arr=[]
chk=0
for x in range(N):
    for y in range(M):
        arr.append([x,y])
        if dfs(x,y,map_list[x][y]):
            chk=1
            break
        arr.pop()

if chk:
    print("Yes")
else:
    print("No")