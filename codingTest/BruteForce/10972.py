#다음순열
"""
1부터 N까지의 수로 이루어진 순열이 있다. 이때 사전순으로 다음에 오는 순열을 구하는 프로그램을 작성하시오
사전 순으로 가장 앞서는 순열은 오름차순으로 이루어진 순열이고, 가장 마지막에 오는 순열은 내림차순으로 이루어진 순열이다
N=3인 경우에 사전 순으로 순열을 나열하려면 다음과 같다

1, 2, 3
1, 3, 2
2, 1, 3
2, 3, 1
3, 1, 2
3, 2, 1

입력
첫째 줄에 N(1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄에 순열이 주어진다.

출력
첫째 줄에 입력으로 주어진 순열의 다음에 오는 순열을 출력한다. 만약, 사전순으로 마지막에 오는 순열인 경우에는 -1을 출력한다.

나의 풀이
순열을 만드는 코드를 작성하고 내가 입력한 순열과 같다면 그 다음 순열을 출력하는 코드를 작성한다
그리고 입력 받은 순열을 내림차순을 한 결과와 같다면 -1일 출력한다
재귀깊이 문제가 발생하여,, 에러가 발생했다 그래서 찾아보니 규칙이 있다고 한다 저번에는 그 규칙을 찾다가 때려쳤는데,,, 있다니 충격적
아무튼 규칙을 잘 설명해주는게 없어서 해석하느라 힘들었다가 손으로 해보면서 이해했다,,:-)

규칙
1) 배열에서 (앞)과 (뒤)를 비교하면서 (앞) < (뒤) 인 것을 찾는다
2) 배열 뒤에서부터 (앞)과 비교하면서 (앞)보다 큰 값을 찾고 그것과 바꾼다 
3) (뒤)의 인덱스부터 끝까지 정렬을 해준다
4) 내림차순으로 정렬한 결과와 입력이 같다면 -1을 출력한다
"""

import sys

def solution():
    if N_list == sorted(N_list, reverse=True):
        print(-1)
        return
    for i in range(N-1,0,-1):
        if N_list[i-1] < N_list[i]:
            for j in range(N-1,0,-1):
                if N_list[i-1] < N_list[j]:
                    N_list[i-1], N_list[j] = N_list[j], N_list[i-1]
                    print(*N_list[:i]+sorted(N_list[i:]))
                    return
                


N=int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().strip().split()))
solution()

"""def solution():
    global chk
    if len(arr)==N:
        if arr==N_list:
            chk=1
            return
        if chk==1:
            chk=2
            print(*arr)
            return
    for i in N_list:
        if i not in arr:
            arr.append(i)
            solution()
            if chk==2:
                return
            arr.pop()

N = int(input())
N_list = list(map(int, input().split()))
arr=[]
chk=0

if N_list == sorted(N_list, reverse=True):
    print(-1)
else:
    solution()"""