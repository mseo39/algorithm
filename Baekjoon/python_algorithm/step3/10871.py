#X보다 작은 수
'''
A에서 X보다 작은 수를 모두 출력
입력
1. 첫째 줄에 N과 X가 주어진다
2. 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다
출력
1. X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다
   X보다 작은 수는 적어도 하나 존재
'''
n, x=map(int, input().split())
for i in input().split():
    if int(i)<x:
        print(i, end=' ')