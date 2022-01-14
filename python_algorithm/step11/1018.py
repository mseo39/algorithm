#체스판 다시 칠하기
'''
MxN 크기의 보드에
어떤 사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 됨
-각 칸이 검은색과 흰색 중 하나로 칠해짐
-변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다
* 두가지 경우
(1) 맨 왼쪽 위 칸이 흰색인 경우
(2) 맨 왼쪽 위 칸이 검은색인 경우

보드를 8x8크기의 체스판으로 자르고 몇 개의 정사각형을 다시 칠할 것이다
다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성
'''
#깊은 복사를 위해 임포트함
import copy

#MxN  크기의 보드를 입력받음
M,N=map(int, input().split())
#빈배열 생성한다
list_1=[]
#열 M만큼 입력을 받는다
for i in range(M):
    #행을 입력받는다
    string=list(input())
    #배열에 추가한다
    list_1.append(string)
#깊은 복사를 위해 메소드를 사용
'''
list_1=[]
list_2=[]
list_1.append(string)
list_2.append(string) 하면 안되는가?

나도 무심코 그런 실수를 했는데 아차했다

위 코드처럼 작성하면 list_1과 list_2는 같은 위치에 저장된
배열을 가리키게 되는 것이므로
list_1으로 값을 변경하면
list_2에도 영향이 간다(같은 것을 공유하기 때문)
'''
list_2=copy.deepcopy(list_1)

#맨 왼쪽 위 칸이 W인 경우
#맨 왼쪽 위 칸이 B인 경우
#두가지의 경우로 규칙에 맞지않아 수정해야 하는 부분은 "M"으로 변경한다
for i in range(M):
    for j in range(N):
        if(((j+i)%2)==0):
            #맨 위 왼쪽 첫번째가 W일 경우
            if(list_1[i][j]=="B"):
                list_1[i][j]="M"
            #맨 위 왼쪽 첫번째가 B일 경우
            if(list_2[i][j]=="W"):
                list_2[i][j]="M"
        elif(((j+i)%2)!=0):
            #맨 위 왼쪽 첫번째가 W일 경우
            if(list_1[i][j]=="W"):
                list_1[i][j]="M"
            #맨 위 왼쪽 첫번째가 B일 경우
            if(list_2[i][j]=="B"):
                list_2[i][j]="M"

min=70 #체스판은 8x8크기로 수정할 개수는 최대 64이다
       #64보다 큰 값으로 지정해준다

#8x8크기로 옮겨가면서 M의 개수를 구한다
for i in range(0,M-7):
    for j in range(0,N-7):
        temp1=0#list_1에서 찾은 수정해야하는 값
        temp2=0#list_2에서 찾은 수정해야하는 값
        for i1 in range(i,i+8):
            #count메서드를 이용하여 M의 개수를 센다
            temp1+=list_1[i1][j:j+8].count("M")
            temp2+=list_2[i1][j:j+8].count("M")
        #둘 중에 작은 것을 찾는다
        temp= temp1 if  temp1<temp2 else temp2
        if(min>temp):
            min=temp
        if(min==0):#0보다 작은 수는 없기 때문에 0이라면 반복문을 끝낸다
            break
# min 값이 그대로 70이라면 수정할게 없으므로
if(min==70):
    #0을 출력한다
    print(0)
#아니라면
else:
    print(min)