# 괄호검사문제

#조건1_ 왼쪽괄호의 개수와 오른쪽 괄호의 개수가 같아야한다
#조건2_ 같은 종류의 괄호에서 왼쪽괄호는 오른쪽 괄호보다 먼저 나와야 한다
#조건3_ 서로 다른 종류의 왼쪽괄호와 오른쪽 괄호 쌍은 서로를 교차하면 안된다

"""
스택을 사용하여 왼쪽괄호들을 삽입하고 오른쪽 괄호를 만나면 스택에서 가장 최근의
왼쪽괄호를 꺼내서 쌍이 맞는지 확인하면 된다

1. 왼쪽 괄호를 만나면 스택에 삽입한다
2. 오른쪽 괄호를 만나면 스택에서 꺼낸 후 짝이 맞는지 확인한다
   - 이때 스택이 비어있지 않아야한다(조건1과 조건2를 위배)
3. 검사가 끝난 후에도 스택에 요소가 남아있으면 안된다(조건1과 조건2를 위배)
"""
class stack():

    def __init__(self):
        self.s=[]

    def isempty(self):
        return len(self.s)==0

    def push(self, item):
        self.s.append(item)

    def pop(self):
        if self.isempty():
            exit()
        else:
            return self.s.pop()
    def peek(self):
        if self.isempty():
            exit()
        else:
            return self.s[-1]
    def size(self):
        return len(self.s)

def check(string):
    s=stack() #스택 객체를 생성한다

    for i in string:
        #왼쪽 괄호를 만났다면
        if (i=="(" or i=="{" or i=="["):
            #스택에 넣어준다
            s.push(i)
        #오른쪽 괄호를 만났다면
        elif (i==")" or i=="}" or i=="]"):
            #스택이 비어져있는지 확인한다(조건1, 조건2)
            if (s.isempty()):
                #비어져있다면_ 실패
                return 0
            #아니라면 (스택에 요소가 있다면)
            #스택에서 꺼낸 괄호와 오른쪽 괄호가 짝이 맞는지 확인한다
            else:
                ch=s.pop()
                if (ch =="(" and i!=")" or ch =="{" and i!="}"):
                    #짝이 맞지않다면_ 실패
                    return 0
    #스택이 비어있는지 확인하기
    if(s.isempty()):
        return 1
    return 0

if(check(input())==1):
    print("성공")
else:
    print("실패")
