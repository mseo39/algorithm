b=0 #통의 개수
c=10 #통의 크기
weight=[7,5,6,4,2,3,7,5] #물건의 크기 리스트
beg=[] #통의 용량은 10

#최초적합
"""
첫번째 통부터 차례로 살펴보며, 가장 먼저 여유가 있는 통에 새물건을 넣는다
"""
for i in weight:
    #기존 통에서 가장 작은 용량을 가진 통의 남은 용량이 물건의 크기보다 크다면
    if(b!=0 and c-min([sum(tmp) for tmp in beg])>i):
        for k in range(b):
            if c-sum(beg[k])>i:
                beg[k].append(i)
                break
    else:
        b+=1
        beg.append([i])

print(beg)
print(b)


"""
for i in weight:
    #기존 통에서 가장 작은 용량을 가진 통의 남은 용량이 물건의 크기보다 크다면
    if(b!=0 and c-min(beg)>i):
        for k in range(b):
            if c-beg[k]>i:
                beg[k]+=i
                break
    else:
        b+=1
        beg.append(i)
print(beg)
print(b)
"""