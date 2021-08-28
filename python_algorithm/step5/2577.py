#숫자의 개수
#각 숫자가 몇 번 나왔는지 저장하기 위해 일차원 배열을 만드는 문제
'''
입력
첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. 
출력
첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다. 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.
'''
'''뭐 이런 방법도 있다,,
a=int(input())
b=int(input())
c=int(input())
num=list(map(int,str(a*b*c)))
for i in range(10):
    print(num.count(i))
'''
a=int(input())
b=int(input())
c=int(input())
num=str(a*b*c)
for i in range(10):
    print(num.count(str(i)))