"""
모든 대문자를 소문자로 변환하고 영숫자가 아닌 문자를 제거한 후 앞뒤로 동일하게 읽는 것,
영숫자 문자에는 문자와 숫자가 포함됩니다
영숫자가 아닌 문자를 제거해야한다
"""
def isPalindrome(self, s):
    s1=s.lower() #소문자로 변경
    s1=list(i for i in s1 if ("0"<=i and i<="9")or("a"<=i and i<="z")) # 정규식으로 불필요한 문자 필터링. s = re.sub('[^a-z0-9]', '', s)
    return s1[::-1]==s1