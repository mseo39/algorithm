# 무인도 여행
"""
메리는 여름을 맞아 무인도로 여행을 가기 위해 지도를 보고 있습니다. 
지도에는 바다와 무인도들에 대한 정보가 표시돼 있습니다. 지도는 1 x 1크기의 사각형들로 이루어진 직사각형 격자 형태이며, 
격자의 각 칸에는 'X' 또는 1에서 9 사이의 자연수가 적혀있습니다. 지도의 'X'는 바다를 나타내며, 숫자는 무인도를 나타냅니다. 

이때, 상, 하, 좌, 우로 연결되는 땅들은 하나의 무인도를 이룹니다. 
지도의 각 칸에 적힌 숫자는 식량을 나타내는데, 상, 하, 좌, 우로 연결되는 칸에 적힌 숫자를 모두 합한 값은 
해당 무인도에서 최대 며칠동안 머물 수 있는지를 나타냅니다. 

어떤 섬으로 놀러 갈지 못 정한 메리는 우선 각 섬에서 최대 며칠씩 머물 수 있는지 알아본 후 놀러갈 섬을 결정하려 합니다.

지도를 나타내는 문자열 배열 maps가 매개변수로 주어질 때, 
각 섬에서 최대 며칠씩 머무를 수 있는지 배열에 오름차순으로 담아 return 하는 solution 함수를 완성해주세요. 
만약 지낼 수 있는 무인도가 없다면 -1을 배열에 담아 return 해주세요.

입출력 예
maps	                            result
["X591X","X1X5X","X231X", "1XXX1"]	[1, 1, 27]
["XXX","XXX","XXX"]	                [-1]

문제 정리
bfs를 통해 하나의 무인도 섬을 탐색하고 무인도의 숫자들을 전부 합친 값을 반환하면 됨
"""

from collections import deque

def solution(maps):
    # 상하좌우 이동 방향 정의
    loc = [[1,0],[0,1],[-1,0],[0,-1]]
    answer = []  # 정답 리스트 초기화
    visited=[[0 for _ in maps[0]]  for _ in maps]  # 방문 여부를 저장할 리스트 초기화
    
    def bfs(x,y):
        q=deque()  # 큐 생성
        q.append([x,y])  # 시작 지점 큐에 추가
        visited[x][y]=1  # 시작 지점 방문 표시
        
        cnt=int(maps[x][y])  # 현재 위치의 값 가져오기
        
        # BFS 탐색
        while q:
            x,y = q.popleft()  # 큐에서 좌표 추출
            for i in loc:  # 상하좌우 이동
                if 0<=x+i[0]<len(maps) and 0<=y+i[1]<len(maps[0]):  # 지도 범위 내에 있는지 확인
                    if maps[x+i[0]][y+i[1]]!="X" and visited[x+i[0]][y+i[1]]==0:  # 섬이 아니고 방문하지 않았는지 확인
                        visited[x+i[0]][y+i[1]]=1  # 방문 표시
                        q.append([x+i[0],y+i[1]])  # 다음 위치 큐에 추가
                        cnt+=int(maps[x+i[0]][y+i[1]])  # 값 누적
        return cnt  # 누적된 값 반환
                    
    # 모든 지점에 대해 탐색
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y]!="X" and visited[x][y]==0:  # 섬이 아니고 방문하지 않았으면
                answer.append(bfs(x,y))  # BFS 탐색 결과를 정답 리스트에 추가
    
    if answer:  # 정답 리스트가 비어있지 않으면
        return sorted(answer)  # 정답 리스트를 정렬하여 반환
    else:  # 정답 리스트가 비어있으면
        return [-1]  # -1 반환
