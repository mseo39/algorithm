## 백트래킹이란?
#완전 탐색을 하는 도중, 현재 탐색이 무의미한 경우 되돌아가는 알고리즘

"""
4-Queen 문제

1. 퀸은 자기가 위치한 행, 열, 대각선으로 움직일 수 있다
2. 어떤 퀸도 다른 퀸을 잡지 못하도록 배치해야 한다

문제가 풀리지 않아 구글링을 해보았다

계속 이상한게 계속 출력되어 뭔가했더니 주석 맨 밑에 프린트한게 있더라,,,
"""
ans=[]
count=0
def go(cnt,N):
    #퀸 4개가 다 놓여져 있다면 끝
    if cnt==N:
        global count
        count+=1
        return
    for i in range(0,N):
        chk=0
        for queen in range(len(ans)):
            if i==ans[queen] or (cnt-queen)**2==(i-ans[queen])**2:
                chk=1
                break
        if chk==0:
            ans.append(i)
            go(cnt+1,N)
            ans.pop()
    return

go(0,int(input()))
print(count)
    

# current=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# ans=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# def go(cnt):
#     if cnt==4:
#         return
#     for i in range(0,4):
#         if current[cnt][i]>=1:
#             return
#         #가로 방향
#         for k in range(0,4):
#             current[cnt][k]+=1
#         #세로 방향
#         for k1 in range(0,4):
#             current[cnt][k]+=1
#         #대각선 방향
#         x=cnt
#         y=i
#         while(x<=3 and y<=3):
#             current[x][y]+=1
#             x+=1
#             y+=1
#         x=cnt
#         y=i
#         while(x>=0 and y>=0):
#             current[x][y]+=1
#             x-=1
#             y-=1
#         x=cnt
#         y=i
#         while(x>=0 and y<=3):
#             current[x][y]+=1
#             x-=1
#             y+=1
#         x=cnt
#         y=i
#         while(x<=3 and y>=0):
#             current[x][y]+=1
#             x+=1
#             y-=1
#         # if sum([arr.count(0) for arr in  current])>=4-cnt:
#         #     print(cnt, i)
#         #     for arr in ans:
#         #         for item in arr:
#         #             print(item, end="")
#         #         print("")
#         #     print("\n")
#         ans[cnt][i]=1
#         go(cnt+1)
#         #가로 방향
#         for k in range(0,4):
#             current[cnt][k]-=1
#         #세로 방향
#         for k1 in range(0,4):
#             current[cnt][k]-=1
#         #대각선 방향
#         x=cnt
#         y=i
#         while(x<=3 and y<=3):
#             current[x][y]-=1
#             x+=1
#             y+=1
#         x=cnt
#         y=i
#         while(x>=0 and y>=0):
#             current[x][y]-=1
#             x-=1
#             y-=1
#         x=cnt
#         y=i
#         while(x>=0 and y<=3):
#             current[x][y]-=1
#             x-=1
#             y+=1
#         x=cnt
#         y=i
#         while(x<=3 and y>=0):
#             current[x][y]-=1
#             x+=1
#             y-=1
#         # if ans[cnt][i] ==1:
#         #     ans[cnt][i]=0
#     return