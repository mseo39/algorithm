#크로아티아 알파벳
#크로아티아 알파벳의 개수를 세는 문제
'''

'''
s=input()
sum=0
sum+=s.count('c=')
sum+=s.count('c-')
sum+=s.count('dz=')
sum+=s.count('d-')
sum+=s.count('lj')
sum+=s.count('nj')
sum+=s.count('s=')
sum+=s.count('z=')
print(len(s)-sum)


'''위의 것을 아래처럼 작성할 수 있음
s=input()
print(len(s)-sum(s.count(i) for i in ['c=','c-','dz=','d-','lj','nj','s=','z=']))
'''
'''
다른방법

c=input().count;print(c('')-1-sum(map(c,['-','=','nj','lj','dz='])))
'''