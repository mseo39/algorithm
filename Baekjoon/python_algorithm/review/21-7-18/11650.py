import sys
tuple=list(tuple(map(int, sys.stdin.readline().split())) for _ in range(int(input())))
tuple.sort(key=lambda x:(x[0],x[1]))
for i in tuple:
    print(*i)