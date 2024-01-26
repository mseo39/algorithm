#combinations
"""
itertools.combinations(array, 7):  # 해당 배열을 7명 중복없이 뽑아준다.
7개의 값을 뽑아서 만들 수 있는 모든 집합을 만들어준다
"""

#최대 공약수와 최소 공배수
"""
def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)
"""

#나머지 식을 확용
"""
x==k%M and y==k%N
-> (k-x)%M==0 and (k-y)%N==0
"""