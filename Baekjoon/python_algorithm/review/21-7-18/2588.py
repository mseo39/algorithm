a=int(input())
b=list(map(int,input()))
sum=0
index=0
b.reverse()
for i in b:
    print(i*a)
    sum=sum+(i*a*(10**index))
    index+=1
print(sum)

#용감하게 시작하는 코딩테스트 2편에 나온 코드
# a = int(input())
# b = int(input())
# arr=[int(i) for i in str(b)]
# arr.reverse()

# for i in range(len(arr)):
#     print(a*arr[i])
# print(a*b)

# 문자열로 변환한 다음 앞에서 한 글자씩 배열에 넣는 코드
# arr = list(map(int, list(String)))
# arr = [int(i) for i in String]