#python 정렬에 대한 정리

'''
reverse()-리스트를 거꾸로 뒤집음
sort()-리스트를 오름차순으로 정렬
sort(reverse=True) - 내림차순으로 정렬
sort(key= ) - key옵션에 지정된 함수의 결과에 따라 정렬
sorted(list) - 정렬된 리스트를 반환
reversed(list) - iterable한 객체를 반환하기 때무네 list()해줘야 됨

'''
#여러 key를 기준으로 정렬하고 싶을 때
"""
✅ 정렬 기본 설명
sort(): 내부를 정렬하고 none을 반환
sorted(): 
새로운 정렬을 만들고 정렬된 것을 반환
입력 자료형과 무방하게 항상 리스트가 반환

✅ x[1]을 기준으로 먼저 내림차순하고 같은 값일 경우에는 x[0]을 기준으로 오름차순으로 정렬
 - 은 내가 정렬하고자 하는 방향의 반대로 정렬해준다
value=sorted(value, key=lambda x : (x[1],-x[0]), reverse=True)

✅ fish[2]-> fish[0] -> fish[1] 순으로 기준을 잡고 정렬을 해준다
fish = sorted(fish, key=(fish[2], fish[0], fish[1]))
"""

#문자열을 정렬
"""
가장 큰 수
   0 1 2 3 4 5 6 7 8
1: 3 3 3
2: 3 0 3 0
3: 3 4 3 4

숫자와 다르게 문자를 비교할 때는 앞에서부터 하나 하나 비교한다
예를 들어 3, 30, 34을 비교한다면
0번 째 3,3,3 비교 다 똑같으니 다음으로
1번 째 3,0,4 이므로 2<1<3으로 정렬된다

numbers=list(map(str,numbers))
numbers.sort(key=lambda x:x*3, reverse=True)
"""