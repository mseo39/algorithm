#A+B - 4 
# #입력이 끝날 때까지 A+B를 출력하는 문제. EOF에 대해 알아 보세요.
'''
입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.
'''
#계속 진행되는 반복문
while 1:
    #입력이 있을 때는 
    try:
        #연산 진행
        a,b=map(int, input().split())
        print(a+b)
    #EOFError가 발생하면 빠져나옴
    except EOFError:
        break