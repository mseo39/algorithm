#덩치
'''
몸무게 x 키 y라면 덩치 (x,y)로 표시
(x,y) (p,q)일 때, x>p and y>q이면 덩치가 더 크다고 표현

두 사람 C와 D의 덩치가 각각 (45, 181), (55, 173)이라면 
몸무게는 D가 C보다 더 무겁고, 키는 C가 더 크므로, 
"덩치"로만 볼 때 C와 D는 누구도 상대방보다 더 크다고 말할 수 없다

덩치등수
자신보다 더 큰 덩치를 가진 사람이 k명이라면 덩치등수는 k+1이 된다
'''
#입력_ 전체사람의 수 N
N=int(input())
N_list=[]
#각 사람의 덩치를 입력받음
for _ in range(N):
    N_list.append(list(map(int, input().split())))

for i in range(N):
    k=0
    for j in range(N):
        #덩치가 크면 k을 1증가
        if(N_list[i][0]<N_list[j][0] and N_list[i][1]<N_list[j][1]):
            k+=1
    print(k+1)
