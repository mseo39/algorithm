#그룹 단어 체커
#조건에 맞는 문자열을 찾는 문제
'''
입력

출력

'''
chr_list=list(input() for _ in range(int(input())))
group_cnt=0
for s in chr_list:
    a=0
    s_list=set(s)
    for c in s_list:
        cnt=0
        for check in s[s.index(c):len(s)+1]:
            if c!=check:
                break
            cnt+=1
        if cnt!=s.count(c):
            a=-1
            break
    if a==0:
        group_cnt+=1
print(group_cnt)
'''
다른방법
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.index):
        result += 1
print(result)
'''