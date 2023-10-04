#별찍기5
answer=int(input())
for i in range(1,answer+1):
    print(" "*(answer-i) + "*"*(2*i-1))