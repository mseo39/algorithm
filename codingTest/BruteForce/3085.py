#사탕게임
"""
상근이는 어렸을 적에 봄보니 게임을 즐겨했디
가장 처음에 NxN크긱에 사탕을 채워 놓는다 사탕의 색은 모두 같지 않을 수도 있다
상근이는 사탕의 색이 다른 인접한 두 칸을 고른다
그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제 모두 같은 색으로 이루어져 있는
가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다
사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오

입력
첫째 줄에 보드의 크기 N이 주어진다
더음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다.
빨간색은 C, 팔란색은 P, 초록색은 Z, 노란색은 Y로 주어진다
사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

나의 풀이
인접한 두 칸을 골라야 한다
-> 상하좌우를 처음에 생각했는데 그러다 보면 똑같은 인접한 두칸이 반복됨
-> 그래서 그림으로 그려보니 좌, 우만 하면 모든 경우의 수를 확인할 수 있음

교환하고 전부 확인해서 가장 긴 사탕을 골랐다

오류가 발생했던 이유
1) 인덱스를 i로 해야하는데 i1으로 해버림,,
2) 그 다음 값과 비교해서 다르면 max_cnt값을 갱신함 그래서 마지막까지 검사하고 갱신하는 부분을 무시해버리는 실수를 함
3) 효율적인 방법을 자꾸 찾으려 그럼 무식하게 생각할 필요가 있는듯
"""
def swap(before, after):
    candy_list[before[1]][before[0]], candy_list[after[1]][after[0]] = candy_list[after[1]][after[0]], candy_list[before[1]][before[0]]

def find(before, after):
    swap(before, after)
    max_cnt=find_logic()
    swap(before,after)
    return max_cnt

def find_logic():
    max_cnt=1
    for i in range(N):
        cnt=1
        for i1 in range(N-1):
            if candy_list[i][i1] == candy_list[i][i1+1]:
                cnt+=1
                max_cnt=max(max_cnt,cnt)
            else:
                cnt=1
        cnt=1
        for i1 in range(N-1):
            if candy_list[i1][i] == candy_list[i1+1][i]:
                cnt+=1
                max_cnt=max(max_cnt,cnt)
            else:
                cnt=1
    return max_cnt

def start():
    # 오른쪽 왼쪽 확인
    location = [[0,1],[1,0]]
    result=[]

    for y in range(N):
        for x in range(N):
            for l in location:
                if 0<=(y+l[0])<N and 0<=(x+l[1])<N:
                    if candy_list[y][x] != candy_list[y+l[0]][x+l[1]]:
                        tmp=find([x,y],[x+l[1],y+l[0]])
                        if tmp==N:
                            return tmp
                        result.append(tmp)
    return max(result)

N=int(input())
candy_list = [list(input()) for _ in range(N)]
print(start())