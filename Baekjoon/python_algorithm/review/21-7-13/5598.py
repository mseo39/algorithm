#카이사르 암호
arr=list(input())
for i in arr:
    print(chr(ord(i)-3),end='') if(ord(i)>=68) else print(chr(ord(i)+23),end='')