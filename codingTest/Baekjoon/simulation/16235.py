# 나무 재테크
"""
시간제한 0.3초
메모리 제한 512MB

부동산 투자로 억대의 돈을 번 상도는 최근 NxN 크기의 땅을 구매했다. 

상도는 손쉬운 땅 관리를 위해 땅을 1x1 크기의 칸으로 나누어 놓았다. 
각각의 칸은 (r, c)로 나타내며, r은 가장 위에서부터 떨어진 칸의 개수, c는 가장 왼쪽으로부터 떨어진 칸의 개수이다. 
r과 c는 1부터 시작한다.

상도는 전자통신공학과 출신답게 땅의 양분을 조사하는 로봇 S2D2를 만들었다. 
S2D2는 1x1 크기의 칸에 들어있는 양분을 조사해 상도에게 전송하고, 
모든 칸에 대해서 조사를 한다. 가장 처음에 양분은 모든 칸에 5만큼 들어있다.

매일 매일 넓은 땅을 보면서 뿌듯한 하루를 보내고 있던 어느 날 이런 생각이 들었다. 나무 재테크를 하자!
나무 재테크란 작은 묘목을 구매해 어느정도 키운 후 팔아서 수익을 얻는 재테크이다. 
상도는 나무 재테크로 더 큰 돈을 벌기 위해 M개의 나무를 구매해 땅에 심었다. 
같은 1x1 크기의 칸에 여러 개의 나무가 심어져 있을 수도 있다.

이 나무는 사계절을 보내며, 아래와 같은 과정을 반복한다.
* 봄
- 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
- 각각의 나무는 나무가 있는 1x1 크기의 칸에 있는 양분만 먹을 수 있다. 
- 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 
- 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.

* 여름
- 봄에 죽은 나무가 양분으로 변하게 된다. 
- 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.

* 가을
- 나무가 번식한다. 번식하는 나무는 나이가 5의 배수이어야 하며, 
- 인접한 8개의 칸에 나이가 1인 나무가 생긴다. 
- 어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다. 
- 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.

* 겨울
- 땅에 양분을 추가한다. 
- 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.

K년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N, M, K가 주어진다.
둘째 줄부터 N개의 줄에 A배열의 값이 주어진다. r번째 줄의 c번째 값은 A[r][c]이다.
다음 M개의 줄에는 상도가 심은 나무의 정보를 나타내는 세 정수 x, y, z가 주어진다. 
처음 두 개의 정수는 나무의 위치 (x, y)를 의미하고, 마지막 정수는 그 나무의 나이를 의미한다.

출력
첫째 줄에 K년이 지난 후 살아남은 나무의 수를 출력한다.
"""
import sys
from collections import deque

loc=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

def spring_summer():
    global total

    for x in range(N):
        for y in range(N):
            if len(Tree[x][y])>0:
                #아이디어
                new_tree=deque()
                tmp=0
                for t in Tree[x][y]:
                    if earth[x][y]>=t:
                        earth[x][y]-=t
                        new_tree.append(t+1)
                    else:
                        total-=1
                        tmp+=(t//2)
                        
                Tree[x][y]=new_tree
                earth[x][y]+=tmp

def fall_winter():
    global total
    tmp=[]
    for x in range(N):
        for y in range(N):
            earth[x][y]+=A[x][y]
            for t in Tree[x][y]:
                if t%5==0:
                    for l in loc:
                        if 0<=x+l[0]<N and 0<=y+l[1]<N:
                            tmp.append([x+l[0], y+l[1]])
    for i in tmp:
        Tree[i[0]][i[1]].appendleft(1)
        total+=1

N, M, K = map(int, sys.stdin.readline().strip().split())

total=0
A=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
Tree=[[deque() for _ in range(N)] for _ in range(N)]
earth = [[5 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x,y,z = map(int, sys.stdin.readline().strip().split())
    Tree[x-1][y-1].append(z)
    total+=1

for k in range(K):
    spring_summer()
    fall_winter()

print(total)