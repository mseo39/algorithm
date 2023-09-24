#N-Queen
"""
N-queen 문제는 크기가 NxN인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오

입력
첫째 줄에 N이 주어진다

출력
첫째 줄에 퀸 N개를 공격할 수 없게 놓는 경우의 수를 출력한다

(cnt, i) 퀸을 놔둘 때,
이미 놓아져있는 퀸들과 비교를 해서 (cnt, i)에 퀸을 놓을 수 있는지 확인을 해야한다
놓을 수 없는 위치는

이미 놓여진 퀸의 위치가 (queen, ans[queen])이고 현재 놓을 퀸의 위치가 (cnt, i)라면

1. 같은 열에 놓으면 안된다(그럼 같은 행은 조건에 안넣도 되냐? 각 행마다 한개씩 놓기 때문에 필요없다)
i랑 ans[queen] 값이 같으면 안된다

2. 이미 놓여진 퀸의 대각선 위치에 두면 안된다
(cnt-queen)**2와 (i-ans[queen])**2가 같다면 대각선 위치에 있다는 것이다
"""

ans = []  # 퀸의 위치를 저장하는 리스트
count = 0  # 해의 개수를 세기 위한 변수

# 퀸을 놓는 함수
def go(cnt, N):
    # 퀸 N개가 다 놓여져 있다면 끝
    if cnt == N:
        global count
        count += 1  # 해의 개수를 1 증가시킴
        return

    # 현재 열에 퀸을 놓아보기
    for i in range(0, N):
        chk = 0
        # 현재 열에 퀸을 놓았을 때, 이전 열의 퀸들과 충돌하는지 확인
        for queen in range(len(ans)):
            if i == ans[queen] or (cnt - queen) ** 2 == (i - ans[queen]) ** 2:
                chk = 1  # 충돌하는 경우 chk를 1로 설정
                break
        if chk == 0:
            ans.append(i)  # 현재 열에 퀸을 놓음
            go(cnt + 1, N)  # 다음 열로 진행
            ans.pop()  # 퀸을 다시 제거하여 다른 경우를 확인

    return

N = int(input("퀸의 개수를 입력하세요: "))
go(0, N)  # 퀸을 놓는 함수 호출
print(count)  # 해의 개수 출력
