#별찍기7
answer=int(input())
for i in range(1,2*answer):
    if (i<=answer):
        print(" "*(answer-i) + "*"*(2*i-1))
    else:
        print(" "*(i-answer) + "*"*(2*(i-(i-answer)*2)-1))