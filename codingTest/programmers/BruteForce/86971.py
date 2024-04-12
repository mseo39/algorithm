# 전력망 둘로 나누기
"""
n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다. 
당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다. 
이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 합니다.

송전탑의 개수 n, 그리고 전선 정보 wires가 매개변수로 주어집니다. 
전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때, 
두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return 하도록 solution 함수를 완성해주세요.

제한사항
* n은 2 이상 100 이하인 자연수입니다.
* wires는 길이가 n-1인 정수형 2차원 배열입니다.
  * wires의 각 원소는 [v1, v2] 2개의 자연수로 이루어져 있으며, 이는 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미합니다.
  * 1 ≤ v1 < v2 ≤ n 입니다.
  *전력망 네트워크가 하나의 트리 형태가 아닌 경우는 입력으로 주어지지 않습니다.

입출력 예
n	wires	                                            result
9	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	3
4	[[1,2],[2,3],[3,4]]	                                0
7	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]	            1
"""
from collections import deque

def solution(n, wires):
    answer = n+1 # 두 전력망의 차이를 저장할 것이기 때문에 최대값을 저장
    
    g=[[] for _ in range(n+1)] # 정점이 1부터 시작하므로 n+1
    
    # bfs 탐색이 쉽도록 그래프를 만들어줌(양방향)
    for i,k in wires:
        g[i].append(k)
        g[k].append(i)
        
    def bfs(v,x,visited):
        q=deque([v])
        # 누가 방문한건지 확인하기 위해 검사 시작한 정점으로
        visited[v]=v
        cnt=1
        
        while q:
            next=q.popleft()
            for t in g[next]:
                #연결 끊긴 부분을 표현하기 위함
                if t==x:
                    continue
                if visited[t]==0: # 아직 방문하지 않았다면
                    q.append(t)
                    visited[t]=v
                    cnt+=1
                else:
                    # 내가 방문한게 아니라면
                    # 전력망을 둘로 나눌 수 없는 것
                    if visited[t]!=v:
                        return False
        return cnt
        
    
    for v in wires:
        visited=[0]*(n+1)
        # 두 정점에서 끊기는 것이기 때문에 두 정점에서 탐색을 시작
        a=bfs(v[0],v[1], visited)
        b=bfs(v[1],v[0], visited)
        
        if False not in [a,b]: # 두개로 나누어 진것이 맞다면
            answer=min(answer, abs(a-b))
    
    return answer