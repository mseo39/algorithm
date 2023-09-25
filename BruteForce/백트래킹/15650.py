 #N과 M (2)
"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.

입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

전 문제와 비슷하지만 오름차순으로 해야 한다는 조건이 생겼다

예전에 풀었던 문제인데 조합 함수를 이용하면 문제를 풀었었다
from itertools import combinations

N,M = map(int, input().split())

num=[i for i in range(1,N+1)]
for i in list(combinations(num,M)):
    print(*i)

그치만 이 문제는 백트래킹으로 풀기 위해서 만들어진 문제이기 때문에 백트래킹으로 풀어보겠다
"""

def go():
    if len(arr)==M:
        print(*arr)
        return
    for i in range(1,N+1):
        if len(arr)==0 or arr[-1]<i and i not in arr:
            arr.append(i)
            go()
            arr.pop()

N,M = map(int,input().split())
arr=[]
go()