# 나무 재테크
"""
시간제한 0.3초
메모리 제한 512MB

"""
import sys
from collections import deque

loc=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

def spring_summer():
    global total

    for x in range(N):
        for y in range(N):
            if len(Tree[x][y])>0:
                #아이디어
                new_tree=deque()
                tmp=0
                for t in Tree[x][y]:
                    if earth[x][y]>=t:
                        earth[x][y]-=t
                        new_tree.append(t+1)
                    else:
                        total-=1
                        tmp+=(t//2)
                        
                Tree[x][y]=new_tree
                earth[x][y]+=tmp

def fall_winter():
    global total
    tmp=[]
    for x in range(N):
        for y in range(N):
            earth[x][y]+=A[x][y]
            for t in Tree[x][y]:
                if t%5==0:
                    for l in loc:
                        if 0<=x+l[0]<N and 0<=y+l[1]<N:
                            tmp.append([x+l[0], y+l[1]])
    for i in tmp:
        Tree[i[0]][i[1]].appendleft(1)
        total+=1

N, M, K = map(int, sys.stdin.readline().strip().split())

total=0
A=[list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
Tree=[[deque() for _ in range(N)] for _ in range(N)]
earth = [[5 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x,y,z = map(int, sys.stdin.readline().strip().split())
    Tree[x-1][y-1].append(z)
    total+=1

for k in range(K):
    spring_summer()
    fall_winter()

print(total)