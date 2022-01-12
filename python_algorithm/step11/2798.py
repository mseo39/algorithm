#블랙잭
'''
카드의 합이 21을 넘지 않는다
카드의 합을 최대한 크게 만든다.

각 카드에 양의 정수
n장의 카드중에서 3장을 고르고 합이 M을 넘지 않도록 한다

5 21
5 6 7 8 9 일때,
5+6 |+7,8,9
5+7 |+8,9
5+8 |+9

내가 검사하고자 하는 다음카드부터 for문을 돌려준다
'''
n,m =map(int, input().split()) #카드개수와 최대 수 입력받음
card=list(map(int, input().split())) #카드 숫자를 입력받아 리스트 생성
max=-1 #카드의 수는 양의 수이므로 음수가 나올 수 없어 max값으로 지정
#for문을 이용하여 모든 경우의 수를 계산한다
for i in range(n):
    #다음카드인 i+1부터 검사
    for j in range(i+1,n):
        #i번째 카드와 j번째 카드를 더해준다
        temp=card[i]+card[j]
        if(temp>m):#m보다 크면 안되기 때문에 탈락
                   #다음 카드도 검사하기 위해 continue를 사용한다
            continue #-break을 사용해 틀림
                     #다음 카드도 검사해야하기 때문에 continue
        #다음카드인 j+1부터 검사
        for k in range(j+1,n):
            #더한값이 max보다 크고 m보다 작거나같다면(게임규칙)
            if(max<temp+card[k] and temp+card[k]<=m):
                max=temp+card[k]#max에 저장
print(max)#for문이 전부 끝다면 max에는 카드3장을 더한 가장 큰값(m보다 작거나 같은)이 저장됨

