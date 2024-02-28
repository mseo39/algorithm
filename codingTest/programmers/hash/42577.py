# 전화번호 목록
"""
전화번호부에 적히 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 
그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한사항
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
같은 전화번호가 중복해서 들어있지 않습니다.

입출력 예제
phone_book	                        return
["119", "97674223", "1195524421"]	false
["123","456","789"]	                true
["12","123","1235","567","88"]	    false

틀린이유
내가 처음에 풀었던 풀이방식이 왜 틀린건지 이해가 안돼서 계속 고민했다
내가 푼 풀이는 모든 전화번호의 길이를 저장해서 최대 1,000,000개가 저장된다
그럼 한 전화번호의 접두사가 다른 곳에도 있는지 검사하기 위해서 최악의 경우 1,000,000번을 거쳐야 한다는 것이다
또한 길이가 겹칠 수 있기 때문에 중복되어 검사할 수도 있다(이개 제일 컸던 것 같다)
-> 그래서 원래 문제에 전화번호 길이를 저장하는 배열을 set을 해주니 통과했다

반면에 다른 사람 풀이는 
"119"가 있으면 "1" 검사 "11"검사 "119"검사 이렇게 했다 이것도 통과가 가능하나

내 풀이는 검사할 길이가 정해져 있어서 그런지 실행속도가 더 빨랐다
"""
def solution(phone_book):
    #길이가 작은 것이 접두사일 확률이 크다고 생각하여 역정렬
    phone_book.sort(key=len, reverse=True)
    #각 전화번호의 길이를 저장하고 
    number_size=set([len(i) for i in phone_book])
    dictionary = dict.fromkeys(phone_book,1)

    for i in phone_book:
        for n in number_size:
            if n<len(i):
                if dictionary.get(i[:n])==1:
                    return False

    return True

print(solution(["12","123","1235","567","88"]))
"""
다른 사람 풀이

def solution(phone_book):
    # 1. Hash map을 만든다
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    # 2. 접두어가 Hash map에 존재하는지 찾는다
    for phone_number in phone_book:
        jubdoo = ""
        for number in phone_number:
            jubdoo += number
            # 3. 접두어를 찾아야 한다 (기존 번호와 같은 경우 제외)
            if jubdoo in hash_map and jubdoo != phone_number:
                return False
    return True
"""