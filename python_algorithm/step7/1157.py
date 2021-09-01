#단어 공부
#주어진 단어에서 가장 많이 사용된 알파벳을 출력하는 문제
'''
입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''
#count()함수를 쓸줄 아는가--인듯
string=input().upper()
a={}
for i in string:
    if i in a:
        a[i]+=1
    else:
        a[i]=1
max=max(a.values())
cnt=0
for key, value in a.items():
    if value==max:
        cnt+=1
        n=key
if cnt==1:
    print(n)
else:
    print("?")

#a.append(s.count('요소'))
#'?'if a.count(max(a))>1
'''
다른방법

s,a=input().lower(),[]
for i in range(97,123):
 a.append(s.count(chr(i)))
print('?'if a.count(max(a))>1 else chr(a.index(max(a))+97).upper())
'''