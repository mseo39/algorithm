#알파벳 개수

"""
알파벳 소문자로만 이루어진 단어 S가 주어진다. 
각 알파벳이 단어에 몇 개가 포함되어 있는지
구하는 프로그램을 작성하시오
"""
import sys
from string import ascii_lowercase

I=sys.stdin.readline
#입력_첫쨰줄에는 단어S가 주어진다. 단어의 길이는 100을 넘지 않으며,
#알파벳 소문자로만 이루어져있다.

#알파벳을 입력받는다
S=I()
#결과를 저장할 리스트
result_list=[]

#소문자 알파벳을 리스트로 만들어주고 for문을 돌려준다
for i in list(ascii_lowercase):
    #count 함수를 사용하여 문자열에 알파벳이 몇개가 있는지 세준다
    result_list.append(S.count(i))
#출력_단어에 포함되어있는 a의 개수, b의 개수,,,,,Z의 개수를
#공백으로 구분해서 출력한다
print(*result_list)
