# 1로 만들기
"""
시간제한 0.15초
메모리 제한 128MB

정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
"""
import sys

def solution():
    arr=[0 for _ in range(n+2)]
    arr[2]=1
    arr[3]=1

    for i in range(4, n+1):
        tmp=[]
        if i%3==0:
            tmp.append(arr[i//3]+1)
        if i%2==0:
            tmp.append(arr[i//2]+1)
        tmp.append(arr[i-1]+1)
        arr[i]=min(tmp)

    print(arr[n])

n= int(sys.stdin.readline())
if n==1:
    print(0)
else:
    solution()

"""
import sys
sys.setrecursionlimit(10**7)
def dp(x):
    if arr[x]!=0:
        return arr[x]
    tmp=[]
    if x%3==0:
        tmp.append(dp(x//3))
    elif x%2==0:
        tmp.append(dp(x//2))
    if x>1:
        tmp.append(dp(x-1))
    arr[x]=min(tmp)+1
    return arr[x]



n= int(sys.stdin.readline())
arr=[0 for _ in range(n+2)]
arr[2]=1
arr[3]=1
dp(n)
print(arr[n])
"""