#별찍기6
answer=int(input())
for i in range(answer):
    print(" "*i + "*"*(2*(answer-i)-1))