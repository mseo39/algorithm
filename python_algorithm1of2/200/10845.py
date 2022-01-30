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
'''
from collections import deque
class queue:
    def __init__(self):
        self.deq=deque()
    
    def push(self,item):
        self.deq.appendleft(item)
    def pop(self):
        if(self.empty()):
            print(-1)
        else:
            self.deq.pop()
    def size(self):
        print(len(self.deq))

    def empty(self):
        if(len(self.deq)==0):
            return 1
        else:
            return 0
    def front(self):
        if(self.empty()):
            print(-1)
        else:
            print(self.deq[0])
    def back(self):
        if(self.empty()):
            print(-1)
        else:
            print(self.deq[-1])
