#부분수열의 합
"""
시간제한 2초
메모리제한 512MB

수열 S가 주어졌을 때, 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 구하는 프로그램을 작성하시오.
예를 들어, S = [5, 1, 2]인 경우에 1, 2, 3(=1+2), 5, 6(=1+5), 7(=2+5), 8(=1+2+5)을 만들 수 있다. 
하지만, 4는 만들 수 없기 때문에 정답은 4이다.

입력
첫째 줄에 수열 S의 크기 N이 주어진다. (1 ≤ N ≤ 20)

둘째 줄에는 수열 S가 주어진다. S를 이루고있는 수는 100,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 출력한다.

내 풀이
combinations을 이용하여 순서없는 조합을 만들고 만든 조합을 다 더해서 해당 인데스에 만들어졌었는지 검사했다
"""
import sys
from itertools import combinations

def result():
    for i in range(1,len(tmp)):
        if tmp[i]==False:
            return i
    return sum(array)+1

N=int(sys.stdin.readline())
array=list(map(int, sys.stdin.readline().rstrip().split()))
tmp=[False for _ in range(sum(array)+1)]

for i in range(1,N+1):
    for t in combinations(array,i):
        tmp[sum(t)]=True

print(result())

"""
다른 사람 풀이

예를 들어 
4
2 1 2 7
일 때, 1 2 2 7 
1<1 num=2
2<2 num=4
4<2 num=6
6<7 break -> 6

N=int(input())
L=sorted(list(map(int,input().split())))
num=1
for i in L:
    if num<i:
        break
    num+=i
print(num)
"""