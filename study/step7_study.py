#count()함수
'''
문자열.count(self, x, __start, __end)
- self 무시가능, x는 찾을 문자열, 찾을 문자, __start<= < __end 는 문자열의 어디부터 어디까지
- 문자열에서 사용하는 메서드
- 문자열 내부에서 특정 문자, 혹은 문자열이 포함되어있는지 계산해서 반환해주는 함수
'''

#find()함수
'''
문자열.find('요소','시작하는 위치(생략하면 0부터)')
- 원하는 문자가 몇번째에 있는지 찾아줌
- 지정된 문자를 찾지 못한다면 -1을 반환함
'''

#리스트에 요소 포함여부 확인
'''
'요소' in '리스트'
있다면 true
없다면 false
'''

#알파벳 대소문자를 구분하지 않고 비교하는 법
'''
lower()메서드를 이용하여 전부 소문자로 만들어준다
upper()메서드를 이용하여 전부 대문자로 만즐어준다
casefold()메서드를 이용하여 전부 소문자로 변환
-> lower()보다 더 많은 문자를 소문자로 변환해줌(ex.독일어)
-> 그래서 lower()보다는 더 효과적임
'''

#알파벳 리스트 만들기
'''
from string import ascii_lowercase
from string import ascii_uppercase

lower_list=list(ascii_lowercase)
upper_list=list(ascii_uppercase)
'''

#알파벳 관련 함수
'''
isupper()- 대문자인지 확인
islower()- 소문자인지 확인
'''

#숫자를 각 자리수의 list로 변환
'''
list(map(int, str('숫자')))
'''

#sorted('리스트 등',key='데이터타입')
'''
이 함수를 사용하면 리스트를 '데이터타입'으로 정렬
'''

#리스트 중복요소 개수 찾기
'''
1. try, except문 사용(ex)
   new_list = {}
    for i in my_list:
        dictionary 내에 존재하는 key값이라면
        try: new_list[i] += 1
        dictionary 내에 없다면
        except: new_list[i] = 1
'''

#strip()함수
'''
- 문자열에서 특정문자를 제거할 수 있음, 여러문자도 가능
- '문자' 안적으면 공백제거
strip('문자')- string의 왼쪽과 오른쪽에서 제거
lstrip('문자')- string의 왼쪽에서 제거
rstrip('문자')- string의 오른쪽에서 제거
'''

#sorted key
'''
sorted(word,key=word.find)
or
sorted(word, key=word.index):
->알파벳을 찾은 순으로 전부 배열해줌
ex) aasdsffa ->aaassdff 
'''

#(1)c=input().count
#   c('')-1
#(2)map(c,['-','=','nj','lj','dz='])
'''
- 정확하게 이해가 가지는 않는다 좀 더 찾아봐야겠다
이것저것 해본 결과,,, 위 코드는
(1)
c=input().count('') 이 코드와 같음을 알 수 있다
(짐작컨데,,, c=input().count를 하면 count메소드를 가진 문자열이 저장되고 c('')하면 c.count('') 실행되나라고 생각한다)
대신 input().count('')만 한다면 문자열의 길이에 +1이 되어서 나오니 -1을 해주는 것이 좋다

(2)
(1)에서 말했듯이 map을 이용하여 ['-','=','nj','lj','dz=']를 c.count('인자')
count 인자로 전달하는 것 같다
저걸 리스트로 만들어서 출력하면 가 문자들리 문자열에 몇개씩 있는지 출력되는 것을 확인할 수 있다
'''