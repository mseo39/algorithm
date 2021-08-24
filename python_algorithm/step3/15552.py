#빠른 A+B
'''
1. input 대신 sys.stdin.readline()를 사용
   단 이때는 개행문까지 입력받기 때문에 문자열을 저장하고 싶은 경우 .rstrip()을 사용
2. 테스트케이스를 하나 받은 뒤 하나 출력해도 된다
'''
import sys

for _ in range(int(sys.stdin.readline())):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)