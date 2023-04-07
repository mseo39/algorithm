#터렛
'''
무한일때, 원점이 같고 반지름이 같을경우
1일 때, 외접하고 내접하는 경우
2일 때, 두 점 사이보다 반지름의 합이 클 경우
'''
n=int(input())
for _ in range(n):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    if ((x1==x2)and(y1==y2)):
        if(r1==r2):
            print(-1)
        else:
            print(0)
    else:
        d=(x1-x2)**2+(y1-y2)**2
        if(d==(r1+r2)**2 or d==(r1-r2)**2):
            print(1)
        elif(d>(r1+r2)**2 or d<(r1-r2)**2):
            print(0)
        else:
            print(2)