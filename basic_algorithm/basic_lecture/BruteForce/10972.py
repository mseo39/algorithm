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
"""

def solution():
    global chk
    if len(arr)==N:
        if arr==N_list:
            chk=1
            return
        if chk==1:
            chk=0
            print(*arr)
            return
    for i in range(1,N+1):
        if i not in arr:
            arr.append(i)
            solution()
            arr.pop()

N = int(input())
N_list = list(map(int, input().split()))
arr=[]
chk=0

if N_list == sorted(N_list, reverse=True):
    print(-1)
else:
    solution()