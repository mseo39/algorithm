#최대히프트리 파이썬으로 구현

'''
파이썬에서는 리스트를 min heap처럼 다룰 수 있게하는 모듈이 존재한다

사용방법

inport heapq

heap=[]
#노드 추가
heapq.heappush(heap,1)
#노드삭제
heapq.heappop(heap)

//따로 정리해두자
'''
class max_heap:
    #초기화
    def __init__(self):
        self.heap_size=1
        self.heap=[]
    #삽입
    def insert_max_heap(self, item):
        i=self.heap_size+1

        while((i!=1) and (item>self.heap[i/2])):
            self.heap[i]=self.heap[i/2]
            i/=2
        self.heap[i]=item

