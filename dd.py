n=int(input())
m=n
freq=1
while n>0:
    n=int(input())
    if n>m:
        m=n
        freq=1
    elif n==m:
        freq+=1
print(m,freq)