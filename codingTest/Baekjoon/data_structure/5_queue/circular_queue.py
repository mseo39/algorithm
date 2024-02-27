#파이썬으로 원형큐 구현하기
'''
- 배열을 선형으로 생각하지말고 원형으로 생각
- fornt와 rear의 값이 배열의 끝인 (max_qsize-1)에 도달하면 다음에 증가되는 값은 0이
  되도록 한다.
- front는 큐의 첫번째 요소의 하나 앞을 rear는 마지막 요소를 가리킨다
- 데이터 삽입시에는 rear가 먼저 증가되고 그 증가된 위치에 데이터를 삽입한다
- 데이터 삭제시에는 front가 증가되고 증가된 위치에서 데이터를 삭제한다
- front==rear라면 원형큐가 비어있는 것이다
- front가 rear보다 하나 앞에 있으면 포화상태이다
'''
#원형큐 크기
max_qsize=10
class circularqueue:
    #원형큐 생성(초기화)
    def __init__(self):
        #front와 rear는 0에서부터 시작
        self.front=0
        self.rear=0
        #리스트생성
        self.items=[None]*max_qsize
    #공백상태
    def is_empty(self):
        #front와 rear이 같다면 원형큐가 빈 것이다
        return self.front==self.rear
    #포화상태
    def is_full(self):
        #front가 rear보다 하나 앞에 있다면 원형큐가 포화상태인 것이다
        return self.front==(self.rear+1)%max_qsize
    #삽입
    def enqueue(self, item):
        #포화상태가 아니라면
        if not self.is_full():
            #rear를 증가하고
            self.rear=(self.rear+1)%max_qsize
            #그 위치에 데이터를 삽입한다
            self.items[self.rear]=item
    #삭제
    def dequeue(self):
        #공백상태가 아니라면
        if not self.is_empty():
            #front를 증가하고
            self.front=(self.front+1)%max_qsize
            #그 위치에 있는 데이터를 반환한다
            return self.items[self.front]
    #맨 앞에 있는 요소를 반환
    def peek(self):
        #공백상태가 아니라면
        if not self.is_empty():
            #맨앞에 있는 요소를 반환
            return self.items[(self.front+1)%max_qsize]