#문제 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
n=int(input()) #수의 N이 주어짐
for i in map(int,input().split()): #N개의 수를 입력한다
    if i!=1:
        for j in range(2,i):
            #소수는 1 또는 자기자신으로만 나눠지는 것,
            #소수가 아닌 것을 찾고 n에서 1을 빼준 뒤 break한다
            if i%j==0 and i!=j:
                n-=1
                break
    else:#1은 소수가 아니므로 제외
        n-=1
print(n)