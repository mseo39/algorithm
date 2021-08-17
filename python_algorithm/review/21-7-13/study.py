#용감하게 시작하는 코딩테스트 1편
#https://covenant.tistory.com/141?category=874690

#나누어 입력받기
a, b=map(int, input().split())

#입력 출력 가속
import sys
N=int(sys.stdin.readline())
sys.stdout.write(N)

#or

from sys import stdin, stdout
input=stdin.readline
print = stdout.write

#우아한 배열 입력
MAP= [list(map(int, input().split())) for _ in range(int(input()))]
#_ - 값을 무시하고 싶은 경우(필요로 하지 않는 경우)
#입력 받은 값을 전부 정수로 바꿔주고 

#정수와 배열이 같은 줄에 들어오는 경우
N, *arr = map(int, input().split())

#문자열을 한 글자씩 배열에 저장
arr= [list(input()) for _ in range(N)]

#배열을 연결해서 출력1
arr=[1,2,3,4]
print("".join(map(str,arr)))
#map(str,arr)-arr에 있는 정수를 str로 변환
#"".join-공백없이 값을 출력

#배열을 연결해서 출력2
print(*arr)