b=0 #통의 개수
c=10 #통의 크기
weight=[7,5,6,4,2,3,7,5] #물건의 크기 리스트
beg=[] #통의 용량은 10

#다음적합
"""
첫번째 통부터 차례로 살펴보며, 가장 먼저 여유가 있는 통에 새물건을 넣는다
"""
for i in weight:
    #직전 통의 남은 용량이 물건의 크기보다 크다면
    if(b!=0 and c-sum(beg[b-1])>=i):
        beg[b-1].append(i)
    else:
        b+=1
        beg.append([i])
print(beg)
print(b)
"""
for i in weight:
    #직전 통의 남은 용량이 물건의 크기보다 크다면
    if(b!=0 and c-beg[b-1]>=i):
        beg[b-1]+=i
    else:
        b+=1
        beg.append(i)
print(beg)
print(b)
"""