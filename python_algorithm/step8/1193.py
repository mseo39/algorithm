#분수찾기
#분수의 순서에서 규칙을 찾는 문제
'''

'''
n=int(input())

i=0
while(n>0):
    i+=1
    n-=i
a=1
b=i
for num in range(-n):
    a+=1
    b-=1
if i%2==0:
    print(str(b)+'/'+str(a))
else:
    print(str(a)+'/'+str(b))
