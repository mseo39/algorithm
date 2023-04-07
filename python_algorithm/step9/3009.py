#네 번째 점
x_list=[] #x좌표를 저장하는 빈배열 생상
y_list=[] #y좌표를 저장하는 빈배열 생상
for _ in range(3): #3개의 점을 받아야 하므로 3번 반복
    x,y=map(int, input().split()) #좌표를 입력받음
    x_list.append(x)#x배열에 추가
    y_list.append(y)#y배열에 추가
#직사각형이므로 총 4개의 좌표중에 x좌표(같은거 2개, 2개)
#y좌표(같은거 2개, 2개)로 1개인 x,y를 찾아서 출력
for i in range(3):
    if(x_list.count(x_list[i])==1):
        x_temp=x_list[i]
    if(y_list.count(y_list[i])==1):
        y_temp=y_list[i]
print(x_temp, y_temp)