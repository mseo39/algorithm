#골드바흐의 추측

#n의 범위는 4<=n<=10000이므로 10000까지 소수를 찾음
arr=[True]*(10000+1)
for i in range(2,10000):
    if arr[i]:
        j=2
        while(i*j<=10000):
            arr[i*j]=False
            j+=1

n=int(input()) #몇개의 숫자를 입력받을 것인지
for _ in range(n): #입력된 n만큼 반복
    num=int(input()) #숫자를 입력받음
    for i in range(2,num):
        if(arr[i]):#소수를 찾고
            temp=num-i#입력받은 숫자-소수
            if(arr[temp]):#나머지 숫자도 소수인지 확인
                min=temp-i#찾은 두개의 소수의 차이를 계산
                #차이가 0보다 작거나 같으면 출력, break
                if (min<=0):
                    print(temp,i)
                    break