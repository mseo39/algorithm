# 주식가격
"""
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
* prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
* prices의 길이는 2 이상 100,000 이하입니다.

입출력 예
prices	         return
[1, 2, 3, 2, 3]	 [4, 3, 1, 1, 0]
"""

# 하나의 원소를 잡고 해당 원소부터 앞에꺼를 계산하는 것
def solution(prices):
    answer=[]
    
    for i in range(len(prices)):
        cnt=0
        for k in range(i+1,len(prices)):
            cnt+=1
            if prices[k]<prices[i]:
                break
        answer.append(cnt)
    
    return answer

# 전부 가격이 떨어지지않는다는 가정하에 초기화하고 떨어지는 부분을 찾으면 값 변경
def solution(prices):
    answer = [i for i in range(len(prices)-1, -1, -1)]
    
    s=[0]
    
    for i in range(1,len(prices)):
        while s and prices[s[-1]] > prices[i]:
            answer[s[-1]]=i-s[-1]
            s.pop()
        s.append(i)
    
    return answer