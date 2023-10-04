#직각삼각형
while(1):
    list_=list(map(int,input().split())) #리스트 입력받기
    list_.sort() # 정렬
    if(list_[0]==0 and list_[1]==0 and list_[2]==0): #0입력 받으면
        break
    #피타고라스 정리
    if(list_[2]*list_[2]==list_[0]*list_[0]+list_[1]*list_[1]):
        print("right")
    else:
        print("wrong")