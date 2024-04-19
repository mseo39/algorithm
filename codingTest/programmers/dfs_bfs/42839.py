# 소수찾기
"""
문제 설명

한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
* numbers는 길이 1 이상 7 이하인 문자열입니다.
* numbers는 0~9까지 숫자만으로 이루어져 있습니다.
* "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

입출력 예
numbers	 return
"17"	 3
"011"	 2

입출력 예 설명

예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
  * 11과 011은 같은 숫자로 취급합니다.

"""

def solution(numbers):
    # 소수를 저장할 빈 리스트 초기화
    answer = []
    # 'numbers' 리스트의 방문 여부를 기록할 리스트 생성
    visited=[0 for _ in numbers]
    # 현재 조합을 임시로 저장할 리스트
    arr=[]

    # 소수인지 확인하는 함수
    def chk():
        k=int("".join(arr))
        if k<=1:
            return False
        for i in range(2,k):
            if k%i==0:
                return False
        return True
    
    # 깊이 우선 탐색 (DFS) 함수로 가능한 모든 숫자 조합 생성
    def dfs():
        nonlocal answer
        for i in range(len(numbers)):
            if visited[i]==0:
                arr.append(numbers[i])
                visited[i]=1
                # 현재 숫자가 소수이고, answer 리스트에 없으면 추가
                if chk() and int("".join(arr)) not in answer:
                    answer.append(int("".join(arr)))
                dfs()
                arr.pop()
                visited[i]=0

    dfs()
    # 생성된 소수의 개수 반환
    return len(answer)

print(solution("011"))