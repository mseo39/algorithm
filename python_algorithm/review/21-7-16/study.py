#용감하게 시작하는 코딩테스트 2편
#https://covenant.tistory.com/142?category=874690

#최대, 최소
import sys
ans=sys.maxsize
arr=[1,2,3,4]
for num in arr:
    if ans>num:
        ans=num
print(ans)
#ans에 최솟값을 저장하고 싶다면 arr에 있는 최댓값보다 큰 값을
#ans에 저장, sys.maxsize을 이용해 임의의 큰 값을 저장해줌

#10진수 -> 2,8,16진수 변환
bin()
oct()
hex()

#2,8,16진수 -> 10진수 변환
int('0b111100',2)
int('0o74',8)
int('0x3c',16)

#진법 연산 예제
for _ in range(int(input())):
    a, b=map(int, input().split())
    print(bin(a)+bin(b))