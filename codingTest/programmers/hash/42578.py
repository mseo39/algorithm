# 의상
"""
코니는 매일 다른 옷을 조합하여 입는것을 좋아합니다.

예를 들어 코니가 가진 옷이 아래와 같고, 
오늘 코니가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 
다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야합니다.

종류	이름
얼굴	동그란 안경, 검정 선글라스
상의	파란색 티셔츠
하의	청바지
겉옷	긴 코트

코니는 각 종류별로 최대 1가지 의상만 착용할 수 있습니다. 예를 들어 위 예시의 경우 동그란 안경과 검정 선글라스를 동시에 착용할 수는 없습니다.
착용한 의상의 일부가 겹치더라도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산합니다.
코니는 하루에 최소 한 개의 의상은 입습니다.
코니가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
코니가 가진 의상의 수는 1개 이상 30개 이하입니다.
같은 이름을 가진 의상은 존재하지 않습니다.
clothes의 모든 원소는 문자열로 이루어져 있습니다.
모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.

입출력 예
clothes	                                                                                     return
[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	  5
[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	              3

나의 풀이
일단 옷의 종류가 문자열이기 때문에 딕셔너리로 만들어서 각 옷들을 종류에 맞게 저장을 해줬다
그 다음 매칭할 수 있는 경우의 수가 얼마나 되나 인데
[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]] 일떄
모자를 선택할 수 있는 경우는 yellow_hat, green_turban 그리고 고르지 않을 경우로 3가지이다
안경을 선택할 수 있는 경우는 blue_sunglasses 그리고 고르지 않을 경우로 2가지이다
그럼 3*2=6이된다 그런데 정답은 6이 아니라 5이다 그 이유는 모자와 안경 둘 다 선택되지 않는 경우는 없기 때문에 -1을 해주는 것이다
즉 (옷의 종류별 개수 +1)을 전부 곱해주고 전부 선택하지 않은 경우를 빼기위해 -1을 해주는 것
"""

def solution(clothes): 
    answer = 1

    dictionary = dict()
    for i in  clothes:
        if dictionary.get(i[1]):
            dictionary[i[1]].append(i[0])
        else:
            dictionary[i[1]]=[i[0]]

    for i in dictionary.values():
        answer*=(len(i)+1)
    return answer-1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))