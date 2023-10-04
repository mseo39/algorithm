#괄호
'''
괄호 문자열은 두 새의 괄호 기호인 (와 ) 만으로 구성되어있는 문자열이다
그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호문자열이라고 부른다

'''
#스택 구현
class stack:
    def __init__(self):
        self.top=[]
    def push(self, item):
        self.top.append(item)
    def pop(self):
        self.top.pop()
    def empty(self):
        if(len(self.top)==0):
            return 1
        else:
            return 0
    def size(self):
        return len(self.top)

def chk(string_):
    stack_=stack()
    for i in string_:
        #왼쪽 괄호를 만나면 push한다
        if(i=="("):
            stack_.push(i)
        #오른쪽 괄호를 만나면
        #비어있는지 확인 후 pop하고 짝이 맞는지 확인
        elif(i==")"):
            if(stack_.empty()):
                return 0
            else:
                stack_.pop()
    if(stack_.empty()):
        return 1
    else:
        return 0

#입력_ T 입력데이터 수
import sys
I=sys.stdin.readline
T=int(I())

for _ in range(T):
    if(chk(I())):
        print("YES")
    else:
        print("NO")