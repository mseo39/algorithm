#구구단
'''
1. n을 입력받음
2. n*1~9 출력
'''
n=int(input())
for i in range(1,10):
    print( '{0} * {1} = {2}'.format(n,i,n*i))