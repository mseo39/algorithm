#숫자의 합
#정수를 문자열로 입력받는 문제. Python처럼 정수 크기에 제한이 없다면 상관 없으나, 예제 3은 일반적인 정수 자료형에 담기에 너무 크다는 점에 주목합시다.
'''
입력
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 
둘째 줄에 숫자 N개가 공백없이 주어진다.
출력
입력으로 주어진 숫자 N개의 합을 출력한다.
'''
#sum(map(int,input()))
sum=0
input()
for i in input():
    sum+=int(i)
print(sum)

'''
다른방법
input();print(sum(map(int,input())))
'''