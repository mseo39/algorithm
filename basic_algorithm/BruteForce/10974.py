#모든순열
"""
N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오

규칙을 찾느라 머리가 뽑힐뻔 했다 약 1시간 넘게 고민하고 찾아보니
permutation 라이브러리를 사용하거나 라이브러리를 사용지않으면 백트래킹을 사용해야 한다고 한다,,,
일단 오늘은 permutation 라이브러리를 이용하고 다음에 백트래킹을 이용해서 풀어보겠다

permutation
리스트, 큐플, 문자열 안에서 r개를 선택
"""
from itertools import permutations

n=int(input())
res=permutations(range(1,n+1),n) # 1~n 중에서 n개를 선택하여 순열을 만듦
for i in res:
    print(*i)
