# 배열돌리기 1
"""
시간제한 1초
메모리제한 512MB

크기가 NxM인 배열이 있을 때, 배열을 돌려보려고 한다. 배열은 다음과 같이 반시계 방향으로 돌려야 한다.

A[1][1] ← A[1][2] ← A[1][3] ← A[1][4] ← A[1][5]
   ↓                                       ↑
A[2][1]   A[2][2] ← A[2][3] ← A[2][4]   A[2][5]
   ↓         ↓                   ↑         ↑
A[3][1]   A[3][2] → A[3][3] → A[3][4]   A[3][5]
   ↓                                       ↑
A[4][1] → A[4][2] → A[4][3] → A[4][4] → A[4][5]
예를 들어, 아래와 같은 배열을 2번 회전시키면 다음과 같이 변하게 된다.

1 2 3 4       2 3 4 8       3 4 8 6
5 6 7 8       1 7 7 6       2 7 8 2
9 8 7 6   →   5 6 8 2   →   1 7 6 3
5 4 3 2       9 5 4 3       5 9 5 4
 <시작>         <회전1>        <회전2>
배열과 정수 R이 주어졌을 때, 배열을 R번 회전시킨 결과를 구해보자.

입력
첫째 줄에 배열의 크기 N, M과 수행해야 하는 회전의 수 R이 주어진다.
둘째 줄부터 N개의 줄에 배열 A의 원소 Aij가 주어진다.

출력
입력으로 주어진 배열을 R번 회전시킨 결과를 출력한다.

풀이
1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 28

일때 [[1, 7, 13, 19, 25, 26, 27, 28, 22, 16, 10, 4, 3, 2], [8, 14, 20, 21, 15, 9]]을 만들어주고 (아래, 오른, 위, 왼)순서로
뒤에 R만큼 떼어서 앞에 붙여준다 근데 여기서 R이 배열의 크기보도 클 수 있기 때문에 R%len(arr[i])하여 계산한다

회전한 결과이다
[[1, 7, 13, 19, 25, 26, 27, 28, 22, 16, 10, 4, 3, 2], [15, 9, 8, 14, 20, 21]]

이것을 아래 오른 위 왼 순서대로 다시 집어 넣어주면 된다
"""
import sys

N,M,R= map(int, sys.stdin.readline().strip().split())
map_list= [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

arr=[[] for _ in range(min(M,N)//2)]
for i in range(min(M,N)//2):
    arr[i].extend([map_list[x][i] for x in range(i,N-i)])
    arr[i].extend(map_list[N-i-1][i+1:M-i])
    arr[i].extend(map_list[x][M-i-1] for x in range(N-i-2,i-1,-1))
    arr[i].extend(map_list[i][M-i-2:i:-1])
for i in range(len(arr)):
    arr[i]=arr[i][len(arr[i])-(R%len(arr[i])):]+arr[i][:len(arr[i])-(R%len(arr[i]))]

for i in range(min(M,N)//2):
    index=0
    #아래로
    for x in range(i,N-i):
        map_list[x][i]=arr[i][index]
        index+=1
      
    #오른쪽으로
    map_list[N-i-1][i+1:M-i]=arr[i][index:index+len(map_list[N-i-1][i+1:M-i])]
    index+=len(map_list[N-i-1][i+1:M-i])

    if index>=len(arr[i]):
        break

    #위로
    for x in range(N-i-2,i-1,-1):
        map_list[x][M-i-1]=arr[i][index]
        index+=1

    #왼쪽으로
    map_list[i][i+1:M-i-1]=arr[i][index+len(map_list[i][i+1:M-i-1]):index-1:-1]
    index+=len(map_list[i][i+1:M-i-1])

for i in map_list:
    print(*i)


"""

print(index)
      print(len(arr[i]))
예전에는 이 방법으로 해결된거 같은데 시간을 줄인 것 같음
import sys

N,M,R= map(int, sys.stdin.readline().strip().split())
map_list= [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
result= [0,0,0]

for _ in range(R):
    for i in range(min(M,N)//2):
        tmp=map_list[i][i]
        #아래로
        for x in range(i,N-i-1):
            tmp1=map_list[x+1][i]
            map_list[x+1][i]=tmp
            tmp=tmp1

        #오른쪽으로
        for y in range(i,M-i-1):
            tmp1=map_list[N-i-1][y+1]
            map_list[N-i-1][y+1]=tmp
            tmp=tmp1

        #위로
        for x in range(N-i-1,i,-1):
            tmp1=map_list[x-1][M-i-1]
            map_list[x-1][M-i-1]=tmp
            tmp=tmp1

        #왼쪽으로
        for y in range(M-i-1,i,-1):
            tmp1=map_list[i][y-1]
            map_list[i][y-1]=tmp
            tmp=tmp1


for i in map_list:
   print(*i)"""