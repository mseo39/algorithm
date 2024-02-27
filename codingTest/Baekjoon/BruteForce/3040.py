#백설공주와 일곱 난쟁이
"""
매일 매일 일곱 난쟁이는 광산으로 일을 하러 간다. 
난쟁이가 일을 하는 동안 백설공주는 그들을 위해 저녁 식사를 준비한다. 
백설공주는 의자 일곱개, 접시 일곱개, 나이프 일곱개를 준비한다.
어느 날 광산에서 아홉 난쟁이가 돌아왔다. 
(왜 그리고 어떻게 아홉 난쟁이가 돌아왔는지는 아무도 모른다) 
아홉 난쟁이는 각각 자신이 백설공주의 일곱 난쟁이라고 우기고 있다.
백설공주는 이런 일이 생길 것을 대비해서, 
난쟁이가 쓰고 다니는 모자에 100보다 작은 양의 정수를 적어 놓았다. 
사실 백설 공주는 공주가 되기 전에 매우 유명한 수학자였다. 
따라서, 일곱 난쟁이의 모자에 쓰여 있는 숫자의 합이 100이 되도록 적어 놓았다.
아홉 난쟁이의 모자에 쓰여 있는 수가 주어졌을 때, 
일곱 난쟁이를 찾는 프로그램을 작성하시오. 
(아홉 개의 수 중 합이 100이 되는 일곱 개의 수를 찾으시오)
"""

"""
첫번째 방법
for문 7개를 사용해서 모든 경우의 수를 구해보는 것이다
근데 7개의 숫자가 중복되면 안되니 set을 이용해서 중복을 제거하고 길이가 7인지 확인한다

def solution(n):
    for i in n:
        for i1 in n:
            for i2 in n:
                for i3 in n:
                    for i4 in n:
                        for i5 in n:
                            for i6 in n:
                                if i+i1+i2+i3+i4+i5+i6==100:
                                    #중복된 값이 있는지 확인하는 코드
                                    if len(set([i,i1,i2,i3,i4,i5,i6]))==7:
                                        return [i,i1,i2,i3,i4,i5,i6]

n=list(int(input()) for _ in range(9))                                
for i in solution(n):
    print(i)
"""

"""
두번째 방법
전부 합한 값 - 100= n이라고 할 때
값 2개를 골라서 n이 되는 값을 찾으면 됩니다
"""
def solution(n):
    for i in n:
        for i1 in n:
            if sum(n)-100==i+i1 and i1!=i:
                return [i,i1]
            
n=list(int(input()) for _ in range(9))     
sub_list=solution(n)                 
for i in n:
    if i in sub_list:
        continue
    print(i)