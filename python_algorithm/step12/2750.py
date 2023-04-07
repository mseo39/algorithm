# 수 정렬하기
'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는
프로그램
'''
#첫째 줄에 수의 개수
N=int(input())
list_=list(int(input()) for _ in range(N))
list_.sort()
for i in list_:
    print(i)
'''
다른 방법( 근데 속도는 같음)
print("\n".join(map(str,list_)))    
'''

'''
속도를 빠르게 하기 위하여
import sys
I= sys.stdin.readline
P= sys.stdout.write를 사용하는 것이 좋다
'''