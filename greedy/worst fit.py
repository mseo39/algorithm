#최악적합
"""
기존의 통 중에서 새 물건이 들어가면 남는 부분이 가장 큰 통에 새 물건을 넣는다.
"""
b=0 #통의 개수
c=10 #통의 크기
weight=[7,5,6,4,2,3,7,5] #물건의 크기 리스트
beg=[] #통의 용량은 10

for i in weight:
    #기존 통에서 가장 작은 용량을 가진 통의 남은 용량이 물건의 크기보다 크다면
    if(b!=0 and c-min([sum(tmp) for tmp in beg])>=i):
        #물건을 넣을 통의 인덱스가 저장될 변수
        select=-1
        #물건을 넣고 가장 큰 남는 크기가 저장될 변수
        maxnum=-1
        for k in range(b):
            if 0<=c-(sum(beg[k])+i)>maxnum:
                maxnum=c-(sum(beg[k])+i)
                select=k
        beg[select].append(i)
    else:
        b+=1
        beg.append([i])
print(beg)
print(b)

"""
for i in weight:
    #기존 통에서 가장 작은 용량을 가진 통의 남은 용량이 물건의 크기보다 크다면
    if(b!=0 and c-min(beg)>=i):
        #물건을 넣을 통의 인덱스가 저장될 변수
        select=-1
        #물건을 넣고 가장 큰 남는 크기가 저장될 변수
        maxnum=-1
        for k in range(b):
            if 0<=c-(beg[k]+i)>maxnum:
                maxnum=c-(beg[k]+i)
                select=k
        beg[select]+=i
    else:
        b+=1
        beg.append(i)
print(beg)
print(b)
"""