#벌집
#벌집이 형성되는 규칙에 따라 벌집의 위치를 구하는 문제
'''
입력

출력

'''
n=int(input())
if n==1:
    print(1)
else:
    i=2
    cnk=1
    while(n>=i):
        i+=6*cnk
        cnk+=1
        
    print(cnk)