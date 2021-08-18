#중위표기식을 후위표기식으로 변환
"""
1. 피연산자는 출력, 연산자는 스택에 넣어준다
2. 스택에 있는 연산자가 내가 현재 처리중인 연산자보다 우선 순위가 높다면
   스택에 있는 연산자를 꺼내준 다음 스택에 넣어준다.
3. 오른쪽 괄호를 만나면 왼쪽 괄호가 삭제될 때 까지 스택에 있는 요소들을 꺼내준다
4. 반복문이 끝난 뒤 스택에 있는 요소들을 다 꺼내준다

연산자 우선순위
0 ( )
1 + -
2 * /

++우선순위가 높거나 같은 경우에는 스택 상단에 있는 요소를 꺼내어 준다

"""
#-----스택 구현
class stack():
    def __init__(self):
        self.s=[]
    
    def isempty(self):
        return len(self.s)==0

    def push(self, item):
        self.s.append(item)

    def pop(self):
        if self.isempty():
            return -1
        else:
            return self.s.pop()
    
    def peek(self):
        if self.isempty():
            return -1
        else:
            return self.s[-1]

#----연산자 우선 순위
def prec(i):
    #숫자가 클수록 우선순위가 높음
    #괄호라면
    if i=="(" or i==")":
        return 0
    elif i=="+" or i=="-":
        return 1
    elif i=="*" or i=="/":
        return 2

#---중위표기식을 후위표기식으로 변환
def infix_to_postfix(string):
    s=stack()
    postfix=[] #후위 표기식 리스트 정의
    for i in string:
        #피연산자라면
        if i!="+" and i!="-" and i!="*" and i!="/" and i!="(" and i!=")":
            #리스트에 넣어줌
            postfix.append(i)
        
        #오른쪽 괄호라면
        elif i==")":
            #왼쪽 괄호를 만날 때 까지 스택에서 요소를 꺼내서 리스트에 넣어줌
            while(1):
                ch=s.pop()
                #왼쪽 괄호를 만나면
                if ch=="(":
                    break
                postfix.append(ch)
        
        #연산자라면
        else:
            #스택이 비어져있지 않고 스택에 있는 연산자의 우선순위가 더 높다면
            ''' 나는 while문이 아니라 if문을 작성했었음 --왜 while문을 써야할까..?'''
            while ((not s.isempty()) and prec(i) <= prec(s.peek())):
                #스택 상단 요소를 꺼내서 리스트에 넣어줌
                postfix.append(s.pop())
            #연산자를 스택에 넣어줌
            s.push(i)
    #스택에 요소가 아직 남아있다면 꺼내서 리스트에 넣어줌
    while(not s.isempty()):
        postfix.append(s.pop())

    return postfix
        


print(*infix_to_postfix(input()))