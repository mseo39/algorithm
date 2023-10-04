#단어뒤집기
'''
문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오
간, 단어의 순서는 바꿀 수 없다.
단어는 영어 알파벳으로만 이루어져 있다
'''

import sys
I=sys.stdin.readline
#입력_ 테스트 케이스의 개수 T가 주어짐
T=int(I())

#문장이 주어지고, 단어의 길이는 최대 20, 문장의 길이는 최대 1000이다
#단어와 단어 사이에는 공백이 하나있다

#스택을 사용하지 않고도 풀 수 있지만 이 문제가 선택된 이유는 스택 때문이므로
#스택을 사용해서도 풀어보았다
#-> 근데 더 오래걸린다

#스택 구현
class stack:
    #초기화
    def __init__(self):
        self.array=[]
    #삽입
    def push(self, item):
        self.array.append(item)
    #삭제
    def pop(self):
        if(self.empty()):
            return 0
        else:
            return(self.array.pop())
    #비어있는지 확인
    def empty(self):
        if(len(self.array)==0):
            return 1
        else:
            return 0
    #길이 확인
    def size(self):
        return len(self.array)

stack_=stack()
#입력한 테스트케이스 만큼 문장을 입력받는다.
for _ in range(T):
    string_=I()
    #단어만큼 반복
    for word in string_.split():
        #단어를 한글자씩 push
        for i in word:
            stack_.push(i)
        for i in range(stack_.size()):
            #스택은 filo이기 때문에
            #넣은 글자들이 반대로 나옴
            print(stack_.pop(), end="")
        print(" ", end="")

'''
스택을 사용하지 않고 푼 것
for _ in range(T):
    string_=I()
    for i in string_.split():
        print(i[::-1], end=" ")
'''