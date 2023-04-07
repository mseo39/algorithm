A,B,V = map(int, input().split())
print((V-A)//(A-B)+1+(((V-A)%(A-B))!=0))
print(1+(((V-A)%(A-B))!=0))