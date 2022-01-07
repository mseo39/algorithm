M,N=map(int, input().split()) #M과 N을 입력 받는다

def chk(num): #소수배열을 반환하는 함수
    #에라토스테네스의 체를 이용하여 소수를 찾는다
    arr=[True] * (num+1)#true를 가진 빈배열을 생성한다
    for i in range(2, num):
        if arr[i]: #값이 true라면
            j=2
            while (i*j <=num):#i의 배수인 인덱스를 전부 False로 바꿔준다
                arr[i*j]=False
                j=j+1
    return arr#배열 반환

arr=chk(M,N)
for i in range(M,N+1):
    if(arr[i] and i!=1):#값이 true이고 i=1아닐때
        print(i)#출력한다