#파이썬으로 단순 연결리스트 구현하기
'''
- 하나의 방향으로만 연결되어 있는 연결리스트
- 단순 연결리스트에서 마지막 노드의 링크는 NULL값을 가진다

1. 노드생성자 = 
2.
3.
4.
5.
6.
7.
'''
class slist:
    class node:
        def __init__(self,item,link):
            self.item=item
            self.next=link
    def __init__(self):
        self.head=0