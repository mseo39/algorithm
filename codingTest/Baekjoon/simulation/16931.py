#겉넓이 구하기
"""
시간제한 1초
메모리제한 512MB

크기가 NxM인 종이가 있고, 종이는 1x1크기의 칸으로 나누어져 있다. 이 종이의 각 칸의 1x1x1 크기의 정육면체를 놓아 3차원 도형을 만들었다
종이의 각 칸에 놓인 정육면체의 개수가 주어졌을 때, 이 도형의 겉넓이를 구하는 프로그램을 작성하시오

위의 그림은 3x3 크기의 종이 위에 정육면체를 놓은 것이고 컽넓이는 60이다

입력
첫째 줄에 종이의 크기 N, M이 주어진다. 둘째 줄부터 N개의 줄에는 종이의 각 칸에 놓인 정육면체의 수가 주어진다.

출력
첫째 줄에 도형의 겉넓이를 출력한다.

나의 풀이
왼쪽에서 오른쪽으로 이동하면서 드러난 면 계산
오른쪽에서 왼쪽으로 이동하면서 드러난 면을 계산하면서

앞에 면과 뒤에면을 비교했을 때 뒤에 면이 더 큰 경우에 두개의 차이만큼 면을 더하면 된다는 것을 알게되었다
또 맨 앞과 맨 뒤 면은 무족건 포함된다
예를 들어 아래와 같이 입력이 들어왔을 때
3 3
1 3 4
2 2 3
1 2 4

왼쪽에서 오른쪽으로 이동하면서 계산해보겠다
1 3 4 를 보면 맨처음 1을 total에 더해주고 1 다음 3과 비교했을 때 2차이 나므로 total은 3
3 다음 4를 비교했을 때 1 차이 나므로 total은 4가 된다
2 2 3, 1 2 4 도 위와 같이 해주면 총 11이 된다

그럼 가장 이해를 쉽게하기 위해 세로 부분을 검사해보겠다
1 2 1을 보면
왼쪽에서 오른쪽: 1과 2를 비교 1차이 이므로 total=1 2외 1을 비교하므로 -1
오른쪽에서 왼쪽: 1과 2를 비교 1차이 이므로 total=1 2외 1을 비교하므로 -1
즉 두개씩 비교하면서 0이 아닌 경우를 빼고 다 더해주면 되는 것이다 그래서 왼쪽에서 오른쪽 오른쪽에서 왼쪽을 따로 나누치 않고 같이 처리
"""
import sys

N,M = map(int, sys.stdin.readline().strip().split())
figure = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
total=0

#가로
for x in range(N):
    total+=figure[x][0]
    for y in range(M-1):
        if figure[x][y]<figure[x][y+1]:
            total+=(figure[x][y+1]-figure[x][y])
        if figure[x][y+1]<figure[x][y]:
            total+=(figure[x][y]-figure[x][y+1])
    total+=figure[x][M-1]

#세로
for y in range(M):
    total+=figure[0][y]
    for x in range(N-1):
        if figure[x][y]<figure[x+1][y]:
            total+=(figure[x+1][y]-figure[x][y])
        if figure[x][y]>figure[x+1][y]:
            total+=(figure[x][y]-figure[x+1][y])
    total+=figure[N-1][y]

#맨 위와 맨 아래는 NxM 이므로 더해줌
print(total+(N*M*2))