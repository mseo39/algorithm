
#파이썬으로 스택 구현하기
"""
1. 스택생성함수
   - 리스트를 생성
2. 삽입함수
   - 요소를 추가한다(append함수 사용)
3. 삭제함수
   - 맨 마지막에 넣어진 요소를 반환하고 삭제(pop함수 사용)
4. 피크함수
   - 맨 마지막에 넣어진 요소를 반환, 삭제하지 않는다([-1], 오른쪽에서 첫번째 값)
5. 공백함수
   - 리스트의 길이가 0이면 비어있는 것이다(len함수를 사용)
6. 개수함수
   - 리스트의 길이가 곧 요소의 개수이다(len함수를 이용)
"""

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
            #-1은 오른쪽에서 첫번째 값을 말함(+는 왼쪽)
            return self.top[-1]

    #리스트의 길이가 0이면 비어있음
    def isEmpty(self):
        return len(self.top)==0

    #길이를 반환
    def size(self):
        return len(self.top)

"""
사용법
1. Stack class의 객체를 생성한다
2. (객체변수.메서드)
"""
a=Stack()
a.push(3)
print(a.peek())
