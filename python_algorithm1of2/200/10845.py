#큐
'''
선입선출 : 먼저 들어온 데이터가 먼저 나가는 구조다
삽입과 삭제가 다른 곳에서 발생
큐에서 삽입이 일어나는 곳을 후단이라고 하고 삭제가 일어나는 곳을 전단이라고 한다

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

파이썬은 큐에 대한 모듈을 제공한다
이것을 시용하기 위하여
 form collections import deque
 deq=deque()
 
 -deque에 존재하는 메서드

 요소를 추가할 때
 (1) 왼쪽 끝에 삽입한다
 deq.appendleft(item)
 (2) 오른쪽 끝에 삽입한다
 deq.append(item)

 요소를 삭제할 때
 (1) 오른쪽 끝 요소를 삭제할 때
 deq.pop()
 (2) 왼쪽 끝 요소를 삭제할 때
 deq.popleft()

배열을 추가할 때
(1) 주어진 배열을 순환하면서 데크의 오른쪽에 추가
deq.extend(array)
(2) 주어진 배열을 순환하면서 데크의 왼쪽에 추가
deq.extendleft(array)

요소 삭제
deq.remove(item)
데크를 num만큼 회전한다
deq.rotate(num)

리스트 처음부터 요소를 삽입하고
리스트 앞에 있는 요소를 삭제

삽입은 뒤에서
삭제는 앞에서 일어나도록 했다

- 큐에 대한 내용을 정리
- 모듈 deque에 대해서도 정리하기
'''
#큐를 사용하기위해서 모듈을 사용
from collections import deque
#입력과 출력을 빠르게 하기위함
import sys

I=sys.stdin.readline
O=sys.stdout.write

class queue:
    #데큐를 만들어줌
    def __init__(self):
        self.deq=deque()
    #삽입
    def Push(self,item):
        self.deq.append(item)
    #삭제
    def Pop(self):
        #비어있으면
        if(self.empty()):
            #-1을 출력
            print(-1)
        #비어있지 않으면
        else:
            #리스트 왼쪽에 있는 요소를 꺼내고 삭제
            print(self.deq.popleft())
    #리스트 크기를 출력
    def size(self):
        print(len(self.deq))
    #리스트가 비어있는
    def empty(self):
        #리스트길이가 0이면 1을 반환
        if(len(self.deq)==0):
            return 1
        #아니라면
        else:
            #0을 빈환
            return 0
    #리스트 앞에 있는 것을 출력
    def front(self):
        if(self.empty()):
            print(-1)
        else:
            print(self.deq[0])
    #리스트 뒤에 있는 것을 출력
    def back(self):
        if(self.empty()):
            print(-1)
        else:
            print(self.deq[-1])

queue_=queue()
#입력_ 첫째줄에 주어지는 명령의 수 N이 주어진다
#둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다
N=int(I().strip())
for _ in range(N):
    com=I().split()
    #입력된 명령에 따라 함수를 실행
    if com[0]=="push":
        queue_.Push(com[1])
    elif com[0]=="pop":
        queue_.Pop()
    elif com[0]=="size":
        queue_.size()
    elif com[0]=="empty":
        if(queue_.empty()):
            print(1)
        else:
            print(0)
    elif com[0]=="front":
        queue_.front()
    elif com[0]=="back":
        queue_.back()