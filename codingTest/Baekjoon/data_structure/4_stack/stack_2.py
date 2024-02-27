#후위표기수식(연산자가 피연산자 뒤에 있는 것)
class stack():
    def __init__(self):
        self.s=[]

    def push(self, item):
        self.s.append(item)
    
    def isempty(self):
        return len(self.s)==0
    
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

def eval(string):
    s=stack()
    for i in string:
        #연산자가 아니라면 (피연산자라면)
        if i!="+" and i!="-" and i!="/" and i!="*":
            s.push(int(i))
        #연산자라면
        else:
            #스택에서 피연산자 꺼내기
            second=s.pop()
            first=s.pop()
            if i=="+":
                s.push(first+second)
            elif i=="-":
                s.push(first-second)
            elif i=="*":
                s.push(first*second)
            elif i=="/":
                s.push(first/second)
    #결과 리턴
    return s.pop()

print(int(eval(input())))
    