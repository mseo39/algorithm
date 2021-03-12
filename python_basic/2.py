#----------비트단위논리연산----------
#~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
#<<(bitwise left shift), >>(bitwise right shift)
#비트단위로 NOT하여 출력하기
#0->1, 1->0
a=int(input())
print(~a) #~a는 -a-1한 값과 같다
#ex) a=2=0010(4bit) ~(0010)=1101=-3 
#비트단위로 AND하여 출력하기
#둘 다 1일때만 1, 나머지 경우는 0
a ,b=input().split()
print(int(a)&int(b))
#비트단위로 OR하여 출력하기 
#둘 중 하나라도 1이라면 1, 나머지 경우는 0
a ,b=input().split()
print(int(a)|int(b))
#비트단위로 XOR하여 출력하기
#a, b 서로 다른 값을 가질경우에만 1, 서로 같은 값을 가진다면 0
a ,b=input().split()
print(int(a)^int(b))

#----------3항 연습----------
#두 정수 중 큰 값을 출력
#"x if C else y" 의 형태로 작성이 된다.
#C : True 또는 False 를 평가할 조건식(conditional expression) 또는 값
#x : C의 평가 결과가 True 일 때 사용할 값
#y : C의 평가 결과가 True 가 아닐 때 사용할 값
a ,b=input().split()
a=int(a)
b=int(b)
print(a if(a>=b) else b)
#세 정수 중 큰 값을 출력
a ,b, c=input().split()
a=int(a)
b=int(b)
c=int(c)
print((a if(a>=b) else b) if ((a if a>b else b)>c) else c)
#세 정수 중 작은 값을 출력
a ,b, c=input().split()
a=int(a)
b=int(b)
c=int(c)
print((b if(a>b) else a) if ((b if a>b else a)<c) else c)

#----------선택실행구조----------
#짝수만 출력하기
a ,b, c=input().split()
a=int(a)
b=int(b)
c=int(c)
if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)