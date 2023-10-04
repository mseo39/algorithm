#파이썬으로 덱 구현하기
'''
- 덱은 double-ended queue의 줄임말로서 큐의 전단과 후단에서 모두 삽입과 삭제가 가능한 큐를 의미
  add_front, delete_front, get_front, add_rear, delete_rear, get_rear가 가능하다
1. init 초기화
2. is_empty 공백상태 확인 front==rear
3. is_full 포화상태 확인 front가 rear보다 한개 앞
4. add_front 덱의 앞에 요소추가 (front-1+size)%size
5. add_rear 덱의 뒤에 요소추가 (rear+1)%size
6. delete_front 덱의 앞에 있는 요소를 반환한 다음 삭제 (front+1)%size
7. delete_rear 덱의 뒤에 있는 요소를 반환한 다음 삭제 (rear-1+size)%size
8. get_front 앞에 있는 요소를 반환
9. get_rear 뒤에 있는 요소를 반환
'''
#덱 크기
size=8
class circulardeque:
  #덱 생성(초기화)
  def init(self):
    self.front=0
    self.rear=0
    self.item=[None]*8
  #공백상태
  def is_empty(self):
    return self.front==self.rear
  #포화상태
  def is_full(self):
    return (self.rear+1)%size==self.front
  #front에 요소 추가
  def add_front(self, item):
    #포화 상태가 아니라면
    if not self.is_full():
      #front가 가리키는 곳은 비어있다 그러니
      #먼저 front가 가리키는 곳에 요소를 넣어주고
      self.item[self.front]=item
      #front를 감소
      self.front=(self.front-1+size)%size
      
  #rear에 요소 추가
  def add_rear(self, item):
    #포화상태가 아니라면
    if not self.is_full():
      #rear를 증가
      self.rear=(self.rear+1)%size
      #rear가 가리키는 곳에 요소를 넣어준다
      self.item[self.rear]=item
  #front 앞에 있는 요소를 삭제해준다
  def delete_front(self):
    #공백상태가 아니라면
    if not self.is_empty():
      #front를 증가
      self.front=(self.front+1)%size
      #front가 가리키는 요소를 반환
      return self.item[self.front]
  #rear가 가리키는 요소를 삭제
  def delete_rear(self):
    #공백상태가 아니라면
    if not self.is_empty():
      #rear이 가리키는 곳은 요소가 저장되어있다 그러니
      #현재 rear이 가리키는 요소를 변수에 저장해주고
      item=self.item[self.rear]
      #rear를 감소
      self.rear=(self.rear-1+size)%size
      #저장한 변수를 반환한다
      return item
  #front 앞에 있는 요소를 반환
  def get_front(self):
    #공백상태라면
    if not self.is_empty():
      #front가 가리키는 곳은 비어져 있음 +1해줘야 함
      return self.item[(self.front+1)%size]
  #rear 뒤에 있는 요소를 반환
  def get_rear(self):
    #공백상태라면
    if not self.is_empty():
      #rear가 가리키는 곳은 비어져있지 않음 그냥 반환
      return self.item[self.rear]