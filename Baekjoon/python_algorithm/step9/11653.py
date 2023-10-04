#정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오
num=int(input())#정수를 입력받는다

while(num>1):
    for i in range(2,num+1): #입력한 범위 내에서
        if(num%i==0):
            num=int(num/i)
            print(i)
            break