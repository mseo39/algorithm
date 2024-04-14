# 단어 변환
"""
두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 
아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.

예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 
"hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 
최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

제한사항
* 각 단어는 알파벳 소문자로만 이루어져 있습니다.
* 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
* words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
* begin과 target은 같지 않습니다.
* 변환할 수 없는 경우에는 0를 return 합니다.

입출력 예
begin	target	words	                                    return
"hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
"hit"	"cog"	["hot", "dot", "dog", "lot", "log"]  	    0
"""
from collections import deque

def solution(begin, target, words):
    # 만약 목표 단어가 주어진 단어 리스트에 없으면, 목표에 도달할 수 없습니다.
    if target not in words:
        return 0
    
    # 'begin'과 'words'의 각 단어에 대해 인접한 단어를 저장하기 위한 사전 'd'를 생성합니다.
    d = {s: [] for s in [begin] + words}
    size = len(begin) - 1
    
    # 'd' 사전에 인접한 단어를 채웁니다.
    for str1 in [begin] + words:
        for str2 in [begin] + words:
            if str1 == str2:
                continue
            # 두 단어가 한 글자만 다른 경우, 인접한 것으로 간주합니다.
            if size == sum(1 for c, c2 in zip(str1, str2) if c == c2):
                d[str1].append(str2)
                d[str2].append(str1)
                
    # BFS 탐색 중 방문한 단어를 추적하기 위한 사전 'visited'를 생성합니다.
    visited = {s: 0 for s in [begin] + words}
    
    # 최단 경로를 찾기 위한 너비 우선 탐색(BFS) 함수를 정의합니다.
    def bfs():
        q = deque()
        visited[begin] = 1
        q.append(begin)

        while q:
            n = q.popleft()
            for i in d[n]:
                if visited[i] == 0:
                    # 시작 단어로부터의 거리를 표시합니다.
                    visited[i] += (visited[n] + 1)
                    # 목표 단어를 찾으면 반환합니다.
                    if i == target:
                        return
                    q.append(i)
    
    # 최단 경로를 찾기 위해 BFS 함수를 호출합니다.
    bfs()
    # 목표 단어까지의 최단 경로 길이를 반환합니다.
    return visited[target] - 1
