# 여행경로
"""
문제 설명

주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 
방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
* 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
* 주어진 공항 수는 3개 이상 10,000개 이하입니다.
* tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
* 주어진 항공권은 모두 사용해야 합니다.
* 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
* 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

입출력 예
tickets	                                                                          return
[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	                              ["ICN", "JFK", "HND", "IAD"]
[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	  ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

입출력 예 설명
예제 #1
["ICN", "JFK", "HND", "IAD"] 순으로 방문할 수 있습니다.

예제 #2
["ICN", "SFO", "ATL", "ICN", "ATL", "SFO"] 순으로 방문할 수도 있지만 
["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] 가 알파벳 순으로 앞섭니다.

느낀점
전에는 그래프가 양방향 그래프로 주어졌고 각 정점에 대해서만 방문했는지를 확인하면 되었는데
이 문제는 a->b 티켓을 사용했는지를 확인해야 했다
그리고 원래는 이중배열로 만들어서 계산을 했었는데 (그렇게 해도 풀릴 것 같지만,,) 한방향 그래프라 그럴 필요가 없었다
무작정 해시로 풀려고 했던 것이 독이었다

특히 알파벳이 앞서 와야 한다고 했는데 나는 미리 정렬을 해두고 경로를 찾았었다 근데 그렇게 안하고 모든 경로를 찾은 뒤에
정렬을 해주면 원하는 값이 맨 앞으로 오게 된다

존내 힘들다ㅠ
"""

def solution(tickets):
    answer = []  # 최종 결과를 저장할 리스트

    # 각 티켓의 방문 여부를 나타내는 리스트 초기화
    visited = [0 for _ in tickets]

    def dfs(arr, dept):
        # 모든 티켓을 사용한 경우 결과 리스트에 추가하고 종료
        if visited.count(1) == len(visited):
            answer.append(arr[:])
            return

        # 모든 티켓을 사용하지 않은 경우에 대한 DFS 탐색
        for i in range(len(tickets)):
            # 현재 티켓이 출발지로 사용되고, 아직 사용되지 않은 경우
            if arr[-1] == tickets[i][0] and visited[i] == 0:
                # 다음 도착지를 경로에 추가하고, 해당 티켓을 사용했음을 표시
                arr.append(tickets[i][1])
                visited[i] = 1
                # DFS 호출 (깊이 우선 탐색)
                dfs(arr, dept + 1)
                # 백트래킹: 다음 도착지로의 탐색이 끝난 후, 경로에서 제거하고 티켓 사용 여부 초기화
                arr.pop()
                visited[i] = 0

    # 초기 출발지를 ICN으로 설정하고 DFS 호출
    dfs(["ICN"], 0)

    # 결과 리스트를 알파벳 순으로 정렬하여 가장 먼저 나오는 경로 반환
    answer.sort()
    return answer[0]

# 테스트
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
