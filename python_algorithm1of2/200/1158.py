#요세푸스 문제
'''
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고
양의 정수 K가 주어진다
이제 순서대로 K번째 사람을 제거한다

0 1 2 3 4 5 6
1 2 3 4 5 6 7
'''
import sys
I=sys.stdin.readline
O=sys.stdout.write
# N과 K를 입력받음
N,K=I().strip().split()
# 1~N으로 리스트 만듦
list_=list(n for n in range(1,int(N)+1))
# 인덱스 i를 0으로 설정
i=0
# 리스트 길이를 나타낼 변수
list_end=int(N)
# list_안에 있는 요소가 전부 삭제되었다면
O("<")
while(True):
    '''
    만약 N은 7이고 K은 3이라고 가정하자
    인덱스 i가 7이 된다면 인덳 0~6에서 벗어나므로
    다시 0이 되어 이어가야한다
    그래서 (인덱스(i))%리스트길이(N)를 해주면 된다

    현재 인덱스(i=0)에서 3번째는 인덱스가 2인것이다
    즉, (K-1)씩 증가 시키면서 i를 갱신
    '''
    i=(i+int(K)-1)%list_end
    list_end-=1
    O(str(list_.pop(i)))
    if(len(list_)==0):
        break
    O(", ")
O(">")