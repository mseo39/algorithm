#17298

'''
크기가 N인 수열 A=A1,A2,....,AN이 있다. 
수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다
그러한 수가 없는 경우에 오큰수는 -1이다

예를 들어, A=[3,5,2,7]인 경우 NGE(1)=5, NGE(2)=7, NGE(3)=7, NGE(4)=-1이다.
A=[9,5,4,8]인 경우에는 NGE(1)=-1, NGE(2)=8, NGE(3)=8, NGE(4)=-1이다
'''
import sys
I=sys.stdin.readline
O=sys.stdout.write
#입력: 첫째줄에 수열 A의 크기 N, 둘째줄에 수열 A의 원소가 주어진단
N=int(I())
A=list(map(int, input().split()))
result_=list(-1 for _ in range(N))
stack_=[-1]
'''
한글자를 기준으로 오른쪽에 있는 리스트에서
왼쪽부터 비교하여 큰것을 출력
'''
for i in range(len(A)):
    if stack_ and A[stack_[-1]]<A[i]:
        for _ in range(len(stack_)-1):
            result_[stack_.pop()]=A[i]
    stack_.append(i)
print(*result_)