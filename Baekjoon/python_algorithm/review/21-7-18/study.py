#용감하게 시작하는 코딩테스트 2편
#https://covenant.tistory.com/142?category=874690

#배열 초기화
N, M=map(int, input().split())
arr=[[0]*N for _ in range(M)]

#배열의 원소로 거꾸로(문제_2588)
arr.reverse()

#배열 원소 갯수(문제_2490)
list.count() #배열에 값이 몇개가 있는 지 찾을 수 있음
str.count() #배열뿐만 아니라 문자열도 가능함

#원소 중복 제거
alpha=['a','b','c','d','e','f','g','a','b','c','d']
alpha=list(set(alpha)) #set은 저장된 원소가 유일함

#2차원 리스트 중복된 값 제거
lst=[[1,2], [1,2],[1]]

print(list(set(map(tuple, lst))))

#배열 정렬(문제_11650)
arr.sort() #오름차순 정렬
arr.sort(reverse=True) #내림차순 정렬
arr.sort(key=lambda x:(x[0],x[1]))
#x[0]을 정렬하고, x[0]값이 같다면 x[1]을 기준으로 오름차순 정렬함