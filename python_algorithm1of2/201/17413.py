#단어 뒤집기 2
'''
문자열 S가 주어졌을 때, 이 문자열에서 단어만 뒤집으려고 한다.

먼저, 문자열 S는 아래와과 같은 규칙을 지킨다.

알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 특수 문자('<', '>')로만 이루어져 있다.
문자열의 시작과 끝은 공백이 아니다.
'<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, 
'<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.
태그는 '<'로 시작해서 '>'로 끝나는 길이가 3 이상인 부분 문자열이고,
'<'와 '>' 사이에는 알파벳 소문자와 공백만 있다. 
단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고, 
연속하는 두 단어는 공백 하나로 구분한다. 
태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.

간단하게 정리하면

태그 안 < >에 있는 글자는 바뀌지 않고
아닌 것은 공백으로 나누어져있는 단어 단위로 거꾸로 바꿔준다

단어를 스택에 넣어서 다시 꺼내서 변경할것인데 어떻게 해야할까

- 단어를 넣을 때
(1) < 를 만날때까지 글자를 넣는다
-> <를 만나면 스택에 있는 글자들을 꺼낸다(스택이 비어있지 않다면)
(2) 빈칸(태그 안에 있는 빈칸 x)을 만날때까지 글자를 넣는다
-> <를 만나면 스택에 있는 글자들을 꺼낸다(스택이 비어있지 않다면)

- 단어를 넣지 않을 때
(1) < 를 만나고 다음 >를 만날 때까지
'''
import sys
I=sys.stdin.readline
O=sys.stdout.write

class stack():
    def init(self):
        self.stack_list=[]
    def Push(self, item):
        self.stack_list.append(item)
    def Pop(self):
        if(self.is_empty()):
            return
        else:
            self.stack_list.pop()
    def is_empty(self):
        if(len(self.stack_list)==0):
            return 1
        else:
            return 0

#-- 다른방법
s = '' # 빈 문자를 만듦
for t in input().split('<'): # < 기준으로 나눔
    if '>' in t: # >가 있는 문자열이라면
        x, y = t.split('>') # >를 기준으로 나눔
        # >로 나누면 인덱스 0은 태그 안 문자열
        # 인덱스 1은 태그 밖 문자열이다
        # x는 그대로 y는 거꾸로 출력
        s+= '<' + x + '>' + ' '.join(map(lambda t: t[::-1], y.split(' ')))
    else: s += ' '.join(map(lambda t: t[::-1], t.split(' ')))
print(s)

'''
---내가 생각한 방법

#문자열을 입력받음
s=I().strip()
stack_=stack()
stack_.init()
#태그 안인지 밖인지 확인하기 위한 것
#태그 안이면 0, 태그 밖이면 1
# <를 만나면1로 병경 >를 만나면 0으로 변경
chk=1
#for문을 이용하여 문자열의 글자 하나씩 확인
for i in s:
    #글자를 그만 넣고 스택에서 글씨를 꺼내야 할때
    if (i=="<" or (i==" " and chk)):
        if(i=="<"):
            chk=0
        if stack_.is_empty()==0:
            # 거꾸로 출력
            O("".join(stack_.stack_list[::-1]))
            stack_.init()
        #띄어쓰기는 그냥 출력 해주자
        if(i==" "):
            O(" ")
        else:
            stack_.Push(i)
    elif(i==">" ):
        chk=1
        stack_.Push(i)
        if stack_.is_empty()==0:
            print("".join(stack_.stack_list), end="")
            stack_.init()
    else:
        stack_.Push(i)
if i==">":
    print("".join(stack_.stack_list), end="")
else:
    print("".join(stack_.stack_list[::-1]), end="")'''