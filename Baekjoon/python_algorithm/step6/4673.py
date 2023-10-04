#셀프 넘버
#함수 d를 정의하여 문제를 해결해 봅시다.
'''
입력 - 없음
출력 - 10000보다 작거나 같은 셀프넘버를 한 줄에 하나씩 출력
'''
not_self_number=[]
self_number=[i for i in range(1,10001)]
def d(num):
    sum=num
    for j in str(i):
        sum+=int(j)
    return sum
for i in range(10001):
    not_self_number.append(d(i))
for n in sorted(set(self_number)-set(not_self_number)):
    print(n)

