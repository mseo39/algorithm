# 베스트앨범
"""
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 
노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.

나의 풀이
문제에서 핵심은 
속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
부분이다 먼저 장르를 정렬해주고 그 다음 곡 내에서 재생횟수를 기준으로 내림차순해주고 같은 값이면 번호를 기준으로 오름차순해주면 되는 것이다

아직 정렬이 너무 익숙하지가 않다 어케 할지는 아는데 방법을 모르는..? 익숙해져야지@!
"""

def solution(genres, plays):
    answer = []
    dictionary = {}

    for i in range(len(genres)):
        if dictionary.get(genres[i]):
            dictionary[genres[i]].append([i,plays[i]])
        else:
            dictionary[genres[i]]=[[i,plays[i]]]

    dictionary = dict(sorted(dictionary.items(), key=lambda x: sum(y[1] for y in x[1]), reverse=True))

    for i, value in dictionary.items():
        value=sorted(value, key=lambda x : (x[1],-x[0]), reverse=True)
        for k in value[:2]:
            answer.append(k[0])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))