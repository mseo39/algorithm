#사분면 고르기

'''
1사분면 (양수, 양수)
2시분면 (음수, 양수)
3사분면 (음수, 음수)
4사분면 (양수, 음수)
'''

a=int(input())
b=int(input())

if a>0 and b>0:
    print(1)
elif  a<0 and b>0:
    print(2)
elif a<0 and b<0:
    print(3)
elif a>0 and b<0:
    print(4)