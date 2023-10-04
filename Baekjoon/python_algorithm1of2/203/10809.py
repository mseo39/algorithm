#알파벳 찾기
"""
알파벳 소문자로만 이루어진 단어 s가 주어진다. 각각의 알파벳에 대해서,
단어에 포함되어있는 경우에는 처음 등장하는 위치를, 포함되어있지 않은
경우에는 -1을 출력하는 프로그램을 작성하십시오

find 함수를 사용하면 찾고자 하는것이 몇번째에 있는지 알려준다
없을 경우에는 -1을 출력해준다
"""

#입력_ 첫째줄에 단어 S가 주어진다
#단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져있다

import sys
from string import ascii_lowercase
I=sys.stdin.readline
S=I()
alphabet_list=list(ascii_lowercase)
#위와 같은 방법으로 알파벳 리스트를 만들어주는 것보다
# alphabet = "abcdefghijklmnopqrstuvwxyz"
#이렇게 만들어주는 것이 훨씬 빨리 돌아간다

#출력_ 각각의 알파벳이 처음 등장하는 위치를 공백ㅇ으로 구분하여 출력한다.

for i in alphabet_list:
    print(S.find(i), end=" ")

    