#설탕 배달
#5와 3을 최소 횟수로 합하여 N을 만드는 문제
'''
N킬로그램을 배달
3킬로그램과 5킬로그램 봉지가 있음
최소 몇봉지로 N킬로그램을 만들 수 있는 구함
만들 수 없다면 -1을 출력
'''
n=int(input())
num=n
cnt=0
while True:
    if num==0:
        print(int(n/3))
        break
    elif num%5==0:
        print(int(num/5)+cnt)
        break
    elif num<0:
        print(-1)
        break
    num-=3
    cnt+=1