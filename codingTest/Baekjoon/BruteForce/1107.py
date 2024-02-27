#리모컨
"""
수빈이는 TV를 보고있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다
리모컨에는 버튼이 0부터 9까지 숫자 +와 -가 있다 +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다
채널 0에서 -를 누른 경우에는 채널이 변하기 않고, 채널은 무한대 만큼 있다

수빈이가 지금 이동하려고 하는 채널은 N이다 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서
버튼을 최소 몇 번 울러야하는지 구하는 프로그램을 작성하시오
수빈이가 지금 보고있는 채널은 100번이다

입력
첫째 줄에 수빈이가 이동하려고 하는 채널 N(0 ≤ N ≤ 500,000)이 주어진다.
둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다.
셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다

출력
첫째 줄에는 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다

나의 풀이
최소로 만들기 위해서 누를 수 있는 버튼을 가지고 만들 수 있는 모든 수열을 만들고 그 중에서 목표 채널 수라 가까운 두개를 정하고 가장 가까이 있는 것을 선택한다
or 
100과의 거리가 더 가까운지 확인해야 할 것 같음

시간초과 날 것같은 기분임,,
시간초과가 나지는 않았지만 메모리 초과가 발생하여 그럼 어떻게 출어야하는지 검색해보았다

n= int(input())
breakdown_n= int(input())
breakdown = list(map(int, input().split())) if breakdown_n!=0 else [11]
number=[i for i in range(10) if i not in breakdown]
result=[]
from itertools import product

def find_min():
    return [] if list(product(number, repeat=len(str(n))-1))[0]==() else list(map(lambda x: int(''.join(map(str, x))),product(number, repeat=len(str(n))-1)))

def find_max():
    return [] if list(product(number, repeat=len(str(n))))[0]==() else list(map(lambda x: int(''.join(map(str, x))),product(number, repeat=len(str(n)))))

def find_max1():
    return [] if list(product(number, repeat=len(str(n))+1))[0]==() else list(map(lambda x: int(''.join(map(str, x))),product(number, repeat=len(str(n))+1)))

result+=([] if len(number)==0 else find_min())
result+=([] if len(number)==0 else find_max())
result+=([] if len(number)==0 else find_max1())

tmp=max([-1] if len(list(filter(lambda x:x<=n, result)))==0 else filter(lambda x:x<=n, result))
tmp1=min([-1] if len(list(filter(lambda x:x>n, result)))==0 else filter(lambda x:x>n, result))


print(min(n-tmp+len(str(tmp)) if tmp!=-1 else 5000001,tmp1-n+len(str(tmp1)) if tmp1!=-1 else 5000001,abs(100-n)))

찾아본 풀이 방법

나는 가장 확률이 높은 곳에서 중복이 가능한 순열을 만들고 그 순열중에서 채널과 가장 가까운 것들만 계산을 하려고 했는데
메모리 초과가 발생했다 그래서 다른 사람 풀이를 찾아보니 그냥 처름부터 가능한 숫자까지 모두 검사를 하는것이다,,,충격,,
검사하는 코드가 시간이 얼마 안결려서 그런걸까..?
이번 풀이를 통해서 메모리를 효율적으로 사용하는 것도 필요하다고 느꼈다

풀이는 다음과 같다
먼저 +,- 버튼으로 이동횟수를 확인한다
그리고 0~1000000 전부 검사한다 채널이 500000이지만 9로만 누를 수 있을 때를 고려하여 1000000까지 검사한다고 한다
그리고 현재 검사하는 숫자에 고장난 숫자가 있는지 확인한다
고장난 번호가 없다면 이동 횟수를 검사하고 최소를 찾는다

맞췄다고는 뜨지만,, 아니 너무 오래걸리잖아??
풀이를 다 찾아봐도 이게 맞는 풀이인것 같다,,
부르트포스는,,멍청하게 생각하고 풀어야 한다,,
"""
n= int(input())
breakdown_n= int(input())
breakdown = list(input().split()) if breakdown_n!=0 else []

min_num=abs(100-n)

for i in range(1000000):
    tmp=str(i)
    for k in range(len(tmp)):
        if tmp[k] in breakdown:
            break
        if k==len(tmp)-1: # 마직막 인덱스가 여기로 왔다면 전부 가능하다는 것이기 때문
            min_num=min(min_num, abs(n-i)+len(tmp))
print(min_num)