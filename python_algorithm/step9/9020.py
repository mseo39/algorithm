#골드바흐의 추측

arr=[True]*(10000+1)
for i in range(2,10000):
    if arr[i]:
        j=2
        while(i*j<=10000):
            arr[i*j]=False
            j+=1

n=int(input())
for _ in range(n):
    num=int(input())
    for i in range(2,num):
        if(arr[i]):
            temp=num-i
            if(arr[temp]):
                min=temp-i
                if (min==0):
                    print(temp,i)
                    break
                if (min<0):
                    print(temp,i)
                    break