#A+B-7
'''
정수 a와 b를 입력 받은 뒤, A+B를 출력
입력
1. 첫째 줄에는 테스트 케이스의 개수가 주어짐
2. 테스트케이스는 한 줄로 이루어져 있으며, a와 b가 주어짐
출력
1. 각 테스트 케이스마다 "Case #x:" 출력한 다음 A+B를 출력
'''
for i in range(1,int(input())+1):
    a,b=map(int, input().split())
    exec("print('Case #{}:'.format(i),a+b)")