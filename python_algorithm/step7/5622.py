#다이얼
#규칙에 따라 문자에 대응하는 수를 출력하는 문제
'''
입력

출력

'''
def minute(c):
    if c=='A' or c=='B' or c=='C':
        return 3
    elif c=='D' or c=='E' or c=='F':
        return 4
    elif c=='G' or c=='H' or c=='I':
        return 5
    elif c=='J' or c=='K' or c=='L':
        return 6
    elif c=='M' or c=='N' or c=='O':
        return 7
    elif c=='P' or c=='Q' or c=='R' or c=='S':
        return 8
    elif c=='T' or c=='U' or c=='V':
        return 9
    elif c=='W' or c=='X' or c=='Y' or c=='Z':
        return 10

sum=0
for i in input():
    sum+=minute(i)
print(sum)
