# 네트워크
"""
문제 설명

네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 
예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 
컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 
따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 
네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

제한사항

컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.

입출력 예

n	computers	                        return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1

나의 풀이
   0  1  2
0 [1, 1, 0], 
1 [1, 1, 0], 
2 [0, 0, 1]

0, 1, 2 를 확인하면 방문하지 않았다면 해당 정점을 선택하고 그 정점에서 연결된 정점들을 방문하면서 방문했다고 기록한다
더 이상 방문할 곳이 없어 함수가 끝나면 그건 하나의 네트워크가 되는 것이다
그럼 다음 방문하지 않은 곳을 찾아보면 위 예시에서는 0을 방문했을 때 0,1이 방문처리 되고 남은 것은 2이다
그래서 2를 방문해주고 인접한 곳이 없으므로 함수를 빠져나온다 이렇게 두 개의 네트워크를 찾을 수 있다
"""

from collections import deque

def bfs(v, computers, visited):
    q=deque([v])
    visited[v]=1

    while q:
        now=q.popleft()
        for i in range(len(computers)):
            if now!=i and computers[now][i]==1 and visited[i]==0:
                visited[i]=1
                q.append(i)



def solution(n, computers):
    answer = 0

    visited=[0 for _ in range(n)]

    for x in range(n):
        if visited[x]==0:
            bfs(x,computers,visited)
            answer+=1

    return answer

print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))