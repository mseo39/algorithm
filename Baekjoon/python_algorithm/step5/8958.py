#OX퀴즈
#OX 퀴즈의 결과를 일차원 배열로 입력받아 점수를 계산하는 문제
'''
입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다.
문자열은 O와 X만으로 이루어져 있다.
출력
각 테스트 케이스마다 점수를 출력한다.
'''
quizs=list( input() for _ in range(int(input())))
for quiz in quizs:
    total=0
    score=0
    for i in quiz:
        if i=='O':
            score+=1
            total+=score
        else:
            score=0
    print(total)