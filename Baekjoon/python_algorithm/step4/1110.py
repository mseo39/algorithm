#더하기 사이클
'''
10보다 작다면 앞에 0을 붙여 두자리 수로 만들고 -> 각 자리의 숫자를 더함
-> 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수
-> 처음 입력했던 숫자가 나올 때까지 반복
'''

#처음에 했던 것 -- 시간초과됨
'''
num=input()
i=0
new=num
while(1):
    i=i+1
    if int(new)<10:
        new='0'+new
    middle=str(int(new[0])+int(new[1]))
    new=new[-1]+middle[-1]
    if new==num:
        print(i)
        break
'''

num= int(input())
new=num
count=0
while 1:
    count+=1
    second=new%10
    new=(int(new/10)+second)%10+second*10
    print(new)
    if new==num:
        print(count)
        break

