#ABCDE
"""
시간제한 2초
메모리 제한 512MB
정답 비율..28% 실화..?

BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.

오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.

A는 B와 친구다.
B는 C와 친구다.
C는 D와 친구다.
D는 E와 친구다.
위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과 친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.
둘째 줄부터 M개의 줄에는 정수 a와 b가 주어지며, 
a와 b가 친구라는 뜻이다. (0 ≤ a, b ≤ N-1, a ≠ b) 같은 친구 관계가 두 번 이상 주어지는 경우는 없다.

출력
문제의 조건에 맞는 A, B, C, D, E가 존재하면 1을 없으면 0을 출력한다.

알고리즘 분류
그래프 이론
그래프 탐색
깊이 우선 탐색
백트래킹
"""

import sys

def solution():
    if len(arr)==5:
        return 1
    for i in M_list[arr[-1]]:
        if i not in arr:
            arr.append(i)
            if solution():
                return 1
            arr.pop()

N, M = map(int, sys.stdin.readline().strip().split())
M_list=[[] for _ in range(N)]
for _ in range(M):
    tmp = list(map(int,sys.stdin.readline().strip().split()))
    M_list[tmp[0]].append(tmp[1])
    M_list[tmp[1]].append(tmp[0])

for i in range(N):
    arr=[i]
    if solution():
        print(1)
        break
    if i==N-1:
        print(0)

"""import sys

def solution(i):
    print(arr)
    if len(arr)==5:
        return 1
    for j in M_list:
        if i in j and j:
            tmp=0
            if j[-1]==i and j[0] not in arr:
                arr.append(j[0])
                tmp = solution(arr[-1])
                arr.pop()
            elif j[0]==i and j[-1] not in arr:
                arr.append(j[-1])
                tmp = solution(arr[-1])
                arr.pop()
            if tmp:
                return 1


N, M = map(int, sys.stdin.readline().strip().split())
M_list=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(M)]
arr=[]

for i in range(N):
    if solution(i):
        print(1)
        break
    if i==N-1:
        print(0)"""