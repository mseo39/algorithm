#최초적합
"""
첫번째 통부터 차례로 살펴보며, 가장 먼저 여유가 있는 통에 새물건을 넣는다
"""

import turtle as t
import random

#랜덤으로 색을 생성
def getRGB():
    r, g, b = 0, 0, 0
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

#그림그리는 함수
#매개변수 위치(x,y), 세로, 가로, 물건 크기, 글씨위치(text_x,text_y), 색 생성 유무
def draw(x,y,height,width,i,text_x,text_y,color_chk):
    #색을 생성해야 한다면
    if(color_chk):
        tmp=getRGB() #색 생성
        t.fillcolor(tmp) #도형 채울 색 지정
        t.pencolor(tmp) # 펜 색깔 지정
    else: #아니라면
        t.fillcolor(1,1,1) #채울 색은 하얀색
        t.pencolor(0,0,0) #펜 색깔은 검정색
    
    t.penup() #이동하는 경로가 그려지지않도록
    t.goto(text_x,text_y) #이동
    t.pendown() #그리기 시작
    t.write(i, font=("Arial", 20, "bold")) #물건 크기 쓰기

    t.penup() #이동하는 경로가 그려지지않도록
    t.goto(x,y) #이동
    t.pendown() #그리기 시작

    t.begin_fill() #색을 채울 도형 시작
    t.right(90) #90도 꺾기
    t.forward(height) #세로만큼 이동
    t.right(90)
    t.forward(width) #가로만큼 이동
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.end_fill() #색을 채울 도형 끝

#그림의 위치
text_x=-100
text_y=50
#
t.shape('turtle')

b=0 #통의 개수
c=10 #통의 크기
weight=[7,5,6,4,2,3,7,5] #물건의 크기 리스트
beg=[] #물건 크기가 저장될 배열

for i in weight:
    #기존 통에서 가장 작은 용량을 가진 통의 남은 용량이 물건의 크기보다 크다면
    if(b!=0 and c-min([sum(tmp) for tmp in beg])>i):
        for k in range(b):
            if c-sum(beg[k])>i:
                #물건 크기 그리기
                draw(k*100,-300*((10-beg[k][-1]-i)/10),300*(i/10),100,i,text_x,text_y,True)
                
                #글씨 위치 이동
                text_x+=30

                #물건 크기 추가
                beg[k].append(i)
                print(beg)

                break
    else:
        #크기가 c인 통 그리기
        draw(b*100,0,300,100,c,b*100,0,False)
        
        #통, 물건 추가
        beg.append([i])
        print(beg)
        
        #물건 크기 그리기
        draw(b*100,-300*((10-i)/10),300*(i/10),100,i,text_x,text_y,True)
        
        #글씨 위치 이동
        text_x+=30

        #통 개수 추가
        b+=1

t.exitonclick()
print(beg)
print(b)

# b=0 #통의 개수
# c=10 #통의 크기
# weight=[7,5,6,4,2,3,7,5] #물건의 크기 리스트
# beg=[] #통의 용량은 10

#최초적합
"""
첫번째 통부터 차례로 살펴보며, 가장 먼저 여유가 있는 통에 새물건을 넣는다
"""
# for i in weight:
#     #기존 통에서 가장 작은 용량을 가진 통의 남은 용량이 물건의 크기보다 크다면
#     if(b!=0 and c-min([sum(tmp) for tmp in beg])>i):
#         for k in range(b):
#             if c-sum(beg[k])>i:
#                 beg[k].append(i)
#                 break
#     else:
#         b+=1
#         beg.append([i])

# print(beg)
# print(b)


"""
for i in weight:
    #기존 통에서 가장 작은 용량을 가진 통의 남은 용량이 물건의 크기보다 크다면
    if(b!=0 and c-min(beg)>i):
        for k in range(b):
            if c-beg[k]>i:
                beg[k]+=i
                break
    else:
        b+=1
        beg.append(i)
print(beg)
print(b)
"""