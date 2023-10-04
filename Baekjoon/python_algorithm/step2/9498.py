s= int(input())
print("A" if(90<=s<=100) else ("B" if(80<=s<=89) else ( "C" if(70<=s<=79) else ("D" if(60<=s<=69) else "F"))))

'''
- 인덱스를 이용

print('FFFFFFDCBAA'[int(input())//10])

90~100 - 몫:10, 9
80~89 - 몫: 8
70~79 - 몫: 7
60~69 - 몫: 6
0~59 - 몫: 5 4 3 2 1 0
'''