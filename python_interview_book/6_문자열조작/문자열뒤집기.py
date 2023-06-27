"""
문자열을 뒤집은 값을 만든다 단 반환하는 것이 아니라 s의 바뀌어야 됨
입력문자열은 문자 배열로 제공된다
"""
def reverseString(s:str)->bool:
    s.reverse()

reverseString(["h","e","l","l","o"])


"""
풀이1 투포인터를 이용한 스왑
def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
"""