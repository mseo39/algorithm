#스택
'''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을
작성하시오

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

import sys
I=sys.stdin.readline
class stack:
    #초기화
    def __init__(self):
        #빈배열을 생성
        self.array=[]
    #정수를 스택에 넣는다
    def push(self,item):
        self.array.append(item)
    #스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다
    #만약 스택에 들어있는 정수가 없을 경우에는 -1을 출력한다
    def pop(self):
        #스택이 비어있다면 -1을 출력
        if(self.isEmpty()):
            print(-1)
        #아니라면 꺼낸 값을 출력
        else:
            print(self.array.pop())
    #스택에 들어있는 정수의 개수를 출력한다
    def size(self):
        return len(self.array)
    #스택이 비어있으면 1, 아니면 0을 출력
    def isEmpty(self):
        #스택이 비어있으면 1
        if(len(self.array)==0):
            return 1
        #스택이 비어있지 않으면 0
        else:
            return 0
    def top(self):
        #만약 스택이 비어있다면 -1을 출력
        if(self.isEmpty()):
            print(-1)
        #아니라면 스택의 가장 위에 있는 정수를 출력한다
        else:
            print(self.array[-1])

#입력_ 첫째 줄에 주어지는 명령의 수 N이 주어진다

N=int(I())
stack_=stack()
for _ in range(N):
    comment=I()
    if "push" in comment:
        temp=comment.split()
        stack_.push(temp[1])
    elif comment=="pop\n":
        stack_.pop()
    elif comment=="size\n":
        print(stack_.size())
    elif comment=="empty\n":
        print(stack_.isEmpty())
    elif comment=="top\n":
        stack_.top()