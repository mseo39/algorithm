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
    '''
    1. heap 크기를 1 늘린다
    2. 루트노드(인덱스=1)가 아니고 삽입할 노드 > 부모노드 일 때
        2-1. 부모노드를 현재 위치로 옮김
        2-2. 인덱스 부모로 이동
    3. while문이 끝나면 i위치에 삽입할 노드를 삽입
    '''
    def insert_max_heap(self, item):
        i=self.heap_size+1

        while((i!=1) and (item>self.heap[i/2])):
            self.heap[i]=self.heap[i/2]
            i/=2
        self.heap[i]=item
    #삭제
    '''
    1. 루트노드를 저장(루트노드를 삭제하기 위함)
    2. 마지막 노드를 저장 -> 힙 트리 크기를 1 줄인다
    3. 부모인덱스=1, 자식인덱스=2
    4. while( 자식인덱스<= 힙 트리 크기 )
        4-1. if( (자식인덱스 < 힙 트리 크기) and ( 왼쪽 자식 < 오른쪽 자식 ) )
            4-1-1. 자식인덱스를 오른쪽으로 변경
        4-2. if( 마지막 노드 > 자식 노드) break
        4-3. 부모 인덱스에 자식을 저장
        4-4. 아래로 이동 부모 <- 자식 자식 <- 자식*2
    5. 부모 인덱스 자리에 마지막 노드를 저장
    '''
    def delete_max_heap(self):
        item=self.heap[1] #루트노드를 저장
        temp=self.heap[self.heap_size] # 마지막 노드를 저장
        self.heap_size-=1 #힙 크기를 1 줄인다
        #부모 인덱스와 자식 인덱스 지정
        parent=1
        child=2
        #자식 인덱스가 힙 트리 크기보다 작거나 같다면
        while(child <= self.heap_size):
            #자식인덱스<힙 트리 크기dlrh(=이라면 오른쪽이 x)
            #왼쪽 자식보다 오른쪽 자식이 더 크다면
            if((child<self.heap_size) and (self.heap[child]<self.heap[child+1] )):
                child+=1 #오른쪽 자식
            #마지막 노드가 자깃노드보다 크다면 더이상 이동할 필요가 없으므로
            #종료한다
            if(temp>self.heap[child]):
                break
            #부모자리에 자식노드를 삽입한다
            self.heap[parent]=self.heap[child]
            #밑으로 이동한다
            parent=child
            child*=2
        #위치를 찾으면 마지막 노드를 삽입한다
        self.heap[parent]=temp

        return item


