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

#----------산술연산----------
#소숫점 이하 넷째 자리에서 반올림
f1, f2 = input().split()
f=float(f1)/float(f2)
print('%.3f'%f)

#6044
f1, f2 = input().split()
a=int(f1)+int(f2)
b=int(f1)-int(f2)
c=int(f1)*int(f2)
d=int(f1)//int(f2)
e=int(f1)%int(f2)
f=int(f1)/int(f2)
print(a)
print(b)
print(c)
print(d)
print(e)
print(round(f,2)) #계속 print('%.2f'%f)이거 써서 틀렸었음 #반올림은 round

a, b, c = input().split()
n=int(a)+int(b)+int(c)
s=n/3
print(n, round(s,2))

#----------비트시프트연산----------
#2진수 형태로 저장되어있는 값을 왼쪽(<<)이나 오른쪽(>>)으로 지정한 비트 수만큼 밀어주면
#2배씩 늘어나거나 1/2로 줄어든다
n = int(input())
print(n<<1)
#ex) a<<1 => a*2^1 a<<2 => a*2^2
#a를 2^b배 만큼 곱한 값을 출력
a, b = input().split()
print(int(a)<<int(b))

#----------비교연산----------
#비교연산자 종류_ <,>,<=,>=,==,!=
#<
a, b = input().split()
print(int(a)<int(b))
#==
a, b = input().split()
print(int(a)==int(b))
#<=
a, b = input().split()
print(int(a)<=int(b))
#!=
a, b = input().split()
print(int(a)!=int(b))
#----------논리연산----------
#bool()을 이용하면 입력된 식이나 값을 평가해 볼 형의 값(true,false)을 출력
#python 언어에서 정수값 0은 false로 그 외의 값은 true로 평가됨
n = int(input())
print(bool(n))
#반대로
n = int(input())
print(bool(not n))
#논리연산 AND연산(boolean AND) #둘 다 참일 경우에만 참
# A B  A&&B
# 0 0   0
# 0 1   0
# 1 0   0
# 1 1   1
a, b = input().split()
print(bool(int(a)) and bool(int(b)))
#논리연산 OR연산(boolean OR) 하나라도 참이면 참
# A B  A||B
# 0 0   0
# 0 1   1
# 1 0   1
# 1 1   1
a, b = input().split()
print(bool(int(a)) or bool(int(b)))
#XOR 참/거짓이 서로 다를 때에만 참
# A B  !A !B A&&!B !A&&B (A&&!B)||(!A&&B)
# 0 0   1  1   0     0           0
# 0 1   1  0   0     1           1
# 1 0   0  1   1     0           1
# 1 1   0  0   0     0           0
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))
#참/거짓이 서로 같을 때에만 참 출력하기
c = bool(int(a))
d = bool(int(b))
print(c==d)
#둘 다 거짓일 경우
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((not c) and (not d))

#3월7일까지 한 것