#2xn 타일링 2
"""
2xn 직사각형을 1x2, 2x1과 2x2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
아래 그림은 2x17 직사각형을 채운 한가지 예이다.

입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
"""
import sys

n=int(sys.stdin.readline())
arr = [0, 1, 3]

for i in range(3, n+1):
    arr.append(arr[i-1] + arr[i-2]*2)

print(arr[n] % 10007)