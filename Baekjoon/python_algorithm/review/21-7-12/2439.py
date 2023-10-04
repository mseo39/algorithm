#별찍기2
answer=int(input())
for i in range(1,answer+1):
    print(" "*(answer-i) + "*"*i)