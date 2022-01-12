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
n,m =map(int, input().split())
card=list(map(int, input().split()))
max=-1
for i in range(n):
    for j in range(i+1,n):
        temp=card[i]+card[j]
        if(temp>m):
            continue #break을 사용해 틀림
                     #다음 카드도 검사해야하기 때문에 continue
        for k in range(j+1,n):
            if(max<temp+card[k] and temp+card[k]<=m):
                max=temp+card[k]
print(max)

