#스타트와 링크

"""
오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 
축구는 평일 오후에 하고 의무 참석도 아니다. 
축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 
이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 
아래와 같은 능력치를 조사했다. 
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다.
팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. 
Sij는 Sji와 다를 수도 있으며, 
i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

입력
첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 
각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 
나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.

1. go()
2. 스타팀과 링크팀의 능력치의 차이가 최솟값을 출력한다
3. 배열에 숫자를 넣을 때 숫자가 이미 배열에 있는 지 확인하고 넣는다


문제가 계속 안풀려서 찾아보니 DFS 개념을 확실하게 하고 풀어야될것 같다
그래서 dfs에 대해서 제대로 공부한 다음에 다시 풀어보겠다
"""

N = int(input())
s=[list(map(int,input().split())) for _ in range(N)]
arr=[]
min=100

"""for i in range(0,N):
    for i1 in range(0,N):
        num.append(s[i][i1]+s[i1][i])"""
"""cnt=0
def go(num,count):
    global cnt
    global min
    if count==N/2:
        for i in arr:
            if min > abs(cnt-i):
                print(count, min, abs(cnt-i))
                min=abs(cnt-i)
        arr.append(cnt)
        return
    for i in range(num,N):
        if s[num][i]==0:
            continue
        print(s[num][i]+s[i][num])
        count+=1
        cnt+=(s[num][i]+s[i][num])
        go(i+1,count)
        count-=1
        cnt-=(s[num][i]+s[i][num])
go(0,0)
print(arr)
print(min)"""


num=[]
for i in range(0,N):
    for i1 in range(0,N):
        if i==i1:
            continue
        num.append(s[i][i1]+s[i1][i])
print(num)

cnt=0

def go(n,count):
    global cnt
    global min
    if count==N/2:
        for i in arr:
            if min > abs(cnt-i):
                print(count, min, abs(cnt-i))
                min=abs(cnt-i)
        arr.append(cnt)
        return
    for i in range(n,len(num)):
        count+=1
        cnt+=num[i]
        go(i+1,count)
        count-=1
        cnt-=num[i]
go(0,0)
print(arr)
print(min)