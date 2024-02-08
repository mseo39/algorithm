#2xn 타일링
"""
시간제한 1초
메모리제한 256MB

2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
아래 그림은 2x5 크기의 직사각형을 채운 한 가지 방법의 예이다.

입력
첫째 줄에 n이 주어진다. (1<=n<=1000)

출력
첫째 줄에 2xn 크기의 직사각형을 채우는 방법의 수를 10007로 나눈 나머지를 출력한다
"""
import sys

def dp(x):
    if tmp[x]!=0:
        return tmp[x]
    else:
        tmp[x]=dp(x-1)+dp(x-2)
        return tmp[x]

N=int(sys.stdin.readline())
tmp= [0 for _ in range(1001)]
tmp[1]=1
tmp[2]=2
print(dp(N)%10007)