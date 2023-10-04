#베르트랑 공준
#자연수 n에 대하여 2n보다 작거나 같은 소수는 
#적어도 하나 존재한다.

#입력된 범위는 1 ≤ n ≤ 123,456 이므로 2부터 2*123456사이의 소수를 담은
#리스트를 생성한다
arr=[True]*(246912+1)
for i in range(2,246912):
    if arr[i]:
        j=2
        while(i*j<=246912):
            arr[i*j]=False
            j+=1

n=int(input())
while(n):
    if (n<=1):
        print(arr[1:2*n].count(True))
    else:
        print(arr[n+1:2*n].count(True))
    n=int(input())