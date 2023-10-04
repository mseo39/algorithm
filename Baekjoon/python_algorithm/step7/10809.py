#알파벳 찾기
#한 단어에서 각 알파벳이 처음 등장하는 위치를 찾는 문제
'''
입력
첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
출력

'''
#find()함수를 사용할 줄 아는가
from string import ascii_lowercase
alpha_list = list(ascii_lowercase)
n=input()

for i in alpha_list:
    if i in n:
        alpha_list[alpha_list.index(i)]=n.index(i)
    else:
        alpha_list[alpha_list.index(i)]=-1
print(*alpha_list)

'''
다른방법
string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(string.find(i), end = ' ')
'''