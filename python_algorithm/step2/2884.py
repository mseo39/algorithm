#알람시계

'''
a,b=map(int,input().split())

1. 
 1-1. b<45라면 a에 1을 빼줘야 함
      b<45가 true라면 a-1
      b<45가 false라면 a-0
 1-2. (a-(b<45))%24
 2. (b-45)%60)
print((a-(b<45))%24,(b-45)%60)
'''
h, m=map(int, input().split())
print((h-1 if m<45 else h)%24, (m-45)%60 )