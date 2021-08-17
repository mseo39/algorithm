#국영수
import sys
arr=list(tuple(sys.stdin.readline().split()) for _ in range(int(input())))
arr.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for i in arr:
    print(i[0])