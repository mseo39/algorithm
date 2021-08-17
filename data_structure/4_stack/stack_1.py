# 괄호검사문제

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
    s=stack()
    for i in string:
        if (i=="("):
            s.push(i)
        elif (i==")"):
            if (s.isempty()):
                return 0
            elif (s.pop() =="(" and i!=")"):
                return 0

    if(s.isempty()):
        return 1
    return 0

if(check(input())==1):
    print("성공")
else:
    print("실패")
