#피보나치 수5
'''
n==0일때 0
n==1일때 1
n>=2일때 f(n-1)+f(n-2)
'''
def fibo(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(int(input())))