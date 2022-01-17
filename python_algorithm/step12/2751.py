#수 정렬하기2
'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램 작성
'''
# 수의 개수를 입력
# 이 수는 절댓값이 1,000,000보다 작거나 같은 정수
N=int(input())
list_=list(abs(int(input())) for _ in range(N))
list_.sort()
for i in list_:
    print(i)