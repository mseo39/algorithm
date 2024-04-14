# 아이템 줍기
"""
문제가 너무 길어서 걍 링크 따라가길,,

맨 처음에는 2배로 안늘리고 하니 이동할 수 없는 곳이지만 길이가 1차이 나니 그냥 이동을 해버리는 문제점이 생겼다
그래서 이걸 늘려줄까 하다가 다른 방법을 삽질했는데,,
그냥 2배가 맞았다ㅎㅎ

"""
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 102x102 크기의 2D 격자를 생성하여 맵을 나타냅니다.
    maps = [[-1 for _ in range(102)] for _ in range(102)]
    
    # 방향: 아래, 오른쪽, 위, 왼쪽
    loc = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
    # 주어진 직사각형에 따라 격자를 채웁니다.
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if x1 < x < x2 and y1 < y < y2:
                    # 직사각형 안에 있는 부분은 통과 가능(0)으로 표시합니다.
                    maps[x][y] = 0
                else:
                    # 경계에 있는 부분이나 직사각형 외부는 통과 불가능(1)으로 표시합니다.
                    if maps[x][y] != 0:
                        maps[x][y] = 1
        
    # 캐릭터와 아이템 위치를 위해 좌표를 두 배로 늘립니다.
    characterX, characterY, itemX, itemY = 2*characterX, 2*characterY, 2*itemX, 2*itemY
    
    def bfs():
        q = deque()
        q.append([characterX, characterY])
        
        while q:
            x, y = q.popleft()
            for l in loc:
                nx = x + l[0]
                ny = y + l[1]
                if 0 <= nx <= 102 and 0 <= ny <= 102 and maps[nx][ny] == 1:
                    maps[nx][ny] += maps[x][y]
                    if nx == itemX and ny == itemY:
                        return
                    q.append([nx, ny])
    bfs()

    return maps[itemX][itemY] // 2

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8))
