#암호 만들기
"""
바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은,
702호에 새로운 보안 시스템을 설치하기로 하였다 이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다
암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다
또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다
즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다
새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자들의 종류는 C가지가 있다고 한다. 이 알파벳을 입수한
민석, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. C개의 문자들이 모두 주어졌을 때,
가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오

입력
첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15) 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다.
주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

출력
각 줄에는 하나씩, 사전식으로 가능성있는 암호를 모두 출력한다

시간제한 2초

문제 정리
1. 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성
2. 증가하는 순서로 배열
3. C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램

나의 풀이:

N과 M 문제들과 비슷한 문제인 것 같아서 백트래킹과 위 조건을 가지고 문제를 풀것이다
모음과 자음의 최소 개수는 모음의 개수를 통해서 해결
오름차순이라는 것과 자음, 모음 최소개수를 통해 시간을 줄이려고 함

틀린 이유
* num > L-2를 검사하는 위치를 출력 함수 이후에 하여 오답이 발생
* 출력형식을 제대로 안보고 띄어쓰기로 출력하게 함
* num > L-2을 빼먹음
"""

def solution(start):
    global num
    #자음은 최소 2개라고 하는데 모음이 L-2보다 크면 최소 2개의 자음을 가지지 못하므로 return한 것
    if num > L-2:
        return
    if len(arr)==L and num>0:
        print("".join(arr))
        return
    for i in range(start,C):
        if C_list[i] in ["a", "e", "i", "o", "u"]:
            num+=1
        arr.append(C_list[i])
        solution(i+1)
        arr.pop()
        if C_list[i] in ["a", "e", "i", "o", "u"]:
            num-=1

#입력 L(암호 길이), C(주어지는 문자 개수)
L, C =map(int, input().split())
#암호가 오름차순이라고 했으므로 미리 오름차순으로 정렬해준다
#그리고 i요소가 선택되면 다음에는 i+1부터 요소를 선택하게 하면 완성된 암호도 오름차순이 된다
C_list = sorted(input().split())
arr=[]
num=0
solution(0)

"""
다른 풀이:
다른 사람 풀이를 보니 조합 라이브러리를 사용해서 만들고
조건에 맞는 것만 출력했다

from itertools import combinations
import sys

input=sys.stdin.readline

L, C = map(int, input().split())
alpha = sorted(input().split())
words = combinations(alpha, L)

for word in words:
    cnt_vow = 0
    for i in word:
        if i in "aeiou":
            cnt_vow += 1

    if cnt_vow >= 1 and L - cnt_vow >= 2:
        print(''.join(word))
"""