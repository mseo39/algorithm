
#파이썬으로 스택 구현하기
class Stack:
    #스택을 생성
    def __init__(self):
        self.top=[]

    #append함수를 사용해서 요소를 추가함
    def push(self, item):
        self.top.append(item)

    #pop함수를 사용해서 마지막 요소를 출력하고 삭제
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print(-1)
            exit()
    
    #맨 위에 있는 값을 출력
    def peek(self):
        if self.isEmpty():
            print("underflow")
            exit()
        else:
            #-1은 오른쪽에서 첫전째 값을 말함(+는 왼쪽)
            return self.top[-1]

    #리스트의 길이가 0이면 비어있음
    def isEmpty(self):
        return len(self.top)==0

    #길이를 반환
    def size(self):
        return len(self.top)