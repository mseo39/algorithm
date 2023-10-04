#부녀회장이 될테야
#층과 거주자 수의 규칙을 찾는 문제
'''
a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지
사람들의 수의 합만큼 데려와 살아야한다

k층에 n호에는 몇 명이 살고 있는가

단, 0층부터 있고 0층의 i호에는 i명 살고 있다

입력
첫 번째 줄에 Test case의 수 T가 주어진다. 

첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다

출력
각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.

제한
1 ≤ k, n ≤ 14
'''
#a가 층 b가 호
for n in range(int(input())):
    a=int(input())+1
    b=int(input())
    array = [[0 for _ in range(b)] for _ in range(a)]
    
    for j in range(a):
        array[j][0]=1
    for i in range(b):
        array[0][i]=i+1
        
    for j in range(1,a):
        for i in range(1,b):
            array[j][i]=array[j][i-1]+array[j-1][i]
    print(array[a-1][b-1])