#10진수를 유니코드 문자로 출력
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
# f=bool(c==d)
print((not c) and (not d))