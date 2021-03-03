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
#큰 따옴표가 들어있는 출력문 git update-git-for-windows
[출처] [git]Logon failed, use ctrl+c to cancel basic credential prompt|작성자 yu-jung31476
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

#----------값변환----------
#정수로 변환
a,b=input().split()
c=int(a)+int(b)
print(c)
#실수로 변환
a=input()
b=input()
c=float(a)+float(b)
print(c)

#----------출력변환----------
#10진수를 16진수로 출력
a=input()
n=int(a)
print('%x'%n)#소문자

a=input()
n=int(a)
print('%X'%n)#대문자

#16진수를 8진수로 출력
a=input()
n=int(a,16) #입력되 a를 16진수로 인식하여 저장
print('%o'%n)

#영문자 1개 입력받아 10진수 유니코드값으로 출력
n=ord(input()) #입력받은 문자를 10진수 유니코드로 변환 후, 저장
print(n)

#10진수를 유니코드 문자로 출력
c = int(input())
print(chr(c))

#-----------산술연산----------
#부호 바꾸기
n = int(input())
print(-n)
#문자1개를 입력받아 다음 문자 출력
c = ord(input())
print(chr(c+1))
#정수 차 구하기
a, b = input().split()
c= int(a)-int(b)
print(c)
#소수 곱
a, b = input().split()
c= float(a)*float(b)
print(c)
#문자열*정수는 문자열을 여러 번 반복한 문자열이 됨
w, n = input().split()
print(w*int(n))

#----------값변환----------
#round(수,자릿수) 원하는 자리까지 반올림
f = float(input())
print(round(f,2))
#소숫점 이하 넷째 자리에서 반올림
f1, f2 = input().split()
f=float(f1)/float(f2)
print('%.3f'%f)