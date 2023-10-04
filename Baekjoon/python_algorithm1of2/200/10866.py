#덱
'''
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys
from collections import deque

I=sys.stdin.readline
O=sys.stdout.write

class queue:
    def __init__(self):
        self.list_=deque()
    def push_front(self, x):
        self.list_.appendleft(x)
    def push_back(self,x):
        self.list_.append(x)
    def pop_front(self):
        if(self.empty()):
            print(-1)
        else:
            print(self.list_.popleft())
    def pop_back(self):
        if(self.empty()):
            print(-1)
        else:
            print(self.list_.pop())
    def size(self):
        print(len(self.list_))
    def empty(self):
        if(len(self.list_)==0):
            return 1
        else:
            return 0
    def front(self):
        if(self.empty()):
            print(-1)
        else:
            print(self.list_[0])
    def back(self):
        if(self.empty()):
            print(-1)
        else:
            print(self.list_[-1])

que=queue()
N=int(I().strip())
for _ in range(N):
    com=I().strip().split()
    if com[0]=="push_back":
        que.push_back(com[1])
    elif com[0]=="push_front":
        que.push_front(com[1])
    elif com[0]=="pop_front":
        que.pop_front()
    elif com[0]=="pop_back":
        que.pop_back()
    elif com[0]=="size":
        que.size()
    elif com[0]=="empty":
        print(que.empty())
    elif com[0]=="front":
        que.front()
    elif com[0]=="back":
        que.back()