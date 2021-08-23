
#파이썬으로 큐 구현하기
"""
큐는 선입선출(First In First Out)
- 뒤에서 데이터 추가, 앞에서 데이터 삭제

1. 큐 생성함수
   - 리스트를 생성
2. 삽입함수
   - 요소를 추가한다(append함수 사용)
3. 삭제함수
   - 맨 처음에 넣어진 요소를 반환하고 삭제(pop함수 사용)
4. 피크함수
   - 맨 처음에 넣어진 요소를 반환, 삭제하지 않는다([0], 첫번째 값)
5. 공백함수
   - 리스트의 길이가 0이면 비어있는 것이다(len함수를 사용)
"""

class queue():
    #큐 생성
    def __init__(self):
        self.q=[]
    
    #리스트 길이가 0이면 비어져 있는 것임
    def is_empty(self):
        return len(self.q)==0
    
    #맨 처음에 넣은 요소를 반환하고 삭제
    def dequeue(self):
        #비어있다면
        if self.is_empty():
            exit()
        #비어있지않다면
        else:
            #맨 앞에있는 요소를 삭제
            #pop(0)으로 첫번째 요소를 삭제한 후 그 뒤에 있는 모든 데이터를 앞으로 한칸씩 옮겨줌
            return self.q.pop(0)

    #리스트 뒤에 요소를 추가
    def enqueue(self, item):
        #append를 이용해 요소를 추가함
        self.q.append(item)

    #리스트의 맨 앞에 있는 요소를 반환(삭제x)
    def peek(self):
        #비어있다면
        if self.is_empty():
            exit()
        #비어있지않다면
        else:
            #리스트의 맨앞에 있는 요소를 반환함
            return self.q[0]