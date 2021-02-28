#----------출력하기----------
print("hello")
#공백을 포함한 문장 출력
print("hello world")
print("hello","world")
#기본 print는 문장을 출력한 후 마지막에 줄을 마꾼다(new line)
print("hello")
print("world")
#작은 따옴표가 들어있는 출력문
print("'hello'")
#큰 따옴표가 들어있는 출력문
print('"hello"')

#6006번 출력형식에 필요한 따옴표와 출력할 문자인 구분하기 위하여 \'와 \"응 리용해 출력
print('\"!@#$%^&*()\'')

#6007번
print('"C:\Download'+'\\'+'\'hello\'.py"')

#6008번
print('print("Hello\\nWorld")')

#----------입출력----------
c=input()
print(c)

#6013
a=input()
b=input()
print(b)
print(a)

#6014
d=input()
print(d)
print(d)
print(d)

#--------
e,f=input().split()
print(e)
print(f)

c1,c2=input().split()
print(c2, c1)

s=input()
print(s,s,s)

a,b=input().split(':')
print(a,b,sep=':')

#6019
y,m,d=input().split('.')
print(d,m,y,sep='-')

#6020
a,b=input().split('-')
print(a,b,sep='')

#6021
s=input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

#6022
s=input()
print(s[0:2], s[2:4], s[4:6])

#6023
h,m,c=input().split(':')
print(m)

#6024
s1,s2=input().split()
print(s1+s2)