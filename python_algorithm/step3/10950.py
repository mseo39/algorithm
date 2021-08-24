#A+B-3
'''
1. 테스트 케이스의 개수를 입력받음
2. 각 줄에 a와 b를 주어짐
3. a+b를 출력
'''
list=list(input() for _ in range(int(input())))
for i in list:
    a,b=map(int,i.split())
    print(a+b)