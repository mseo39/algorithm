#스택 수열
'''
스택은 기존적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다
스택은 자료를 넣는 push입구와 자료를 뽑는  pop입구가 같아 제일 나중에 들어간 자료가 제일
먼저 나오는 LIFO 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자

임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지
있다면 어떤 순서로 push와 pop연산을 수행해야 하는지를 알아낼 수 있다

이를 계산하는 프로그램을 작성
'''
#입력_n이 주어진다
import sys
from unittest import result
I=sys.stdin.readline
n=int(I())

list_=list(int(I()) for _ in range(n))
list1_=list(i for i in range(1,n+1))

index_=0
index1_=0
result_=[]
stack_=[0,]
'''
1. 스택 상단에 있는 요소와 입력된 배열,
인덱스기 index_인 요소와 비교
1-1. 같다면 pop
1-2. 다르면 push

그렇다면 수열이 안만들어지는 조건이 무엇일까....

'''

while(index1_!= n):
    if(list_[index_]==stack_[-1]):
        stack_.pop()
        result_.append("-")
        index_+=1
        continue

    stack_.append(list1_[index1_])
    index1_+=1
    result_.append("+")

if(list_[index_:]==stack_[n:0:-1]):
    for i in result_:
        print(i)
    for _ in range(len(stack_)-1):
        print("-")
else:
    print("NO")

