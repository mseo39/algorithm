#별찍기
'''
첫째줄부터 N번째 줄까지 출력
'''
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)