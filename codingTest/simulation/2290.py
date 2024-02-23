#LCD Test
"""
시간제한 2초
메모리제한 128MB

지민이는 새로운 컴퓨터를 샀다. 하지만 새로운 컴퓨터에 사은품으로 온 LC-디스플레이 모니터가 잘 안나오는 것이다
지민이의 친한친구인 지환이는 지민이의 새로운 모니터를 위해 테스트 할 수 있는 프로그램을 만들기로 하였다

입력
첫째 줄에 두 개의 정수 s와 n이 들어온다. (1 ≤ s ≤ 10, 0 ≤ n ≤ 9,999,999,999)이다. 
n은 LCD 모니터에 나타내야 할 수 이며, s는 크기이다.

출력
길이가 s인 '-'와 '|'를 이용해서 출력해야 한다. 
각 숫자는 모두 s+2의 가로와 2s+3의 세로로 이루어 진다. 나머지는 공백으로 채워야 한다. 
각 숫자의 사이에는 공백이 한 칸 있어야 한다.

      --   --        --   --   --   --   --   --  
   |    |    | |  | |    |       | |  | |  | |  | 
   |    |    | |  | |    |       | |  | |  | |  | 
      --   --   --   --   --        --   --       
   | |       |    |    | |  |    | |  |    | |  | 
   | |       |    |    | |  |    | |  |    | |  | 
      --   --        --   --        --   --   --  

      --   --        --   --   --   --   --   --
   |    |    | |  | |    |       | |  | |  | |  |
   |    |    | |  | |    |       | |  | |  | |  |
      --   --   --   --   --        --   --
   | |       |    |    | |  |    | |  |    | |  |
   | |       |    |    | |  |    | |  |    | |  |
      --   --        --   --        --   --   --

"""
import sys

s,n = sys.stdin.readline().strip().split()
s=int(s)
result = [[' '] * ((s+2+1)*len(n)-1) for _ in range(2*s+3)]
x=1

def top_width(x):
    for t in range(x,x+s):
        result[0][t]='-'
def mid_width(x):
    for t in range(x,x+s):
        result[(2*s+3)//2][t]='-'
def bottom_width(x):
    for t in range(x,x+s):
        result[2*s+3-1][t]='-'
def top_height(x):
    for y in range(1,1+s):
        result[y][x]='|'

def bottom_height(x):
    for y in range(2+s,2+s+s):
        result[y][x]='|'


for k in n:
    if k=='1':
        x+=s
        top_height(x)
        bottom_height(x)
        x+=2

    elif k=='2':
        bottom_height(x)
        x+=1
        top_width(x)
        mid_width(x)
        bottom_width(x)
        
        x+=s
        top_height(x)
        x+=2
    elif k=='3':
        x+=1
        top_width(x)
        mid_width(x)
        bottom_width(x)
        x+=s
        top_height(x)
        bottom_height(x)
        x+=2
    elif k=='4':
        top_height(x)
        x+=1
        mid_width(x)
        x+=s
        top_height(x)
        bottom_height(x)
        x+=2
    elif k=='5':
        top_height(x)
        x+=1
        top_width(x)
        mid_width(x)
        bottom_width(x)
        x+=s
        bottom_height(x)
        x+=2
    elif k=='6':
        top_height(x)
        bottom_height(x)
        x+=1
        top_width(x)
        mid_width(x)
        bottom_width(x)
        x+=s
        bottom_height(x)
        x+=2
    elif k=='7':
        x+=1
        top_width(x)
        x+=s
        top_height(x)
        bottom_height(x)
        x+=2
    elif k=='8':
        top_height(x)
        bottom_height(x)
        x+=1
        top_width(x)
        mid_width(x)
        bottom_width(x)
        x+=s
        top_height(x)
        bottom_height(x)
        x+=2
    elif k=='9':
        top_height(x)
        x+=1
        top_width(x)
        mid_width(x)
        bottom_width(x)
        x+=s
        top_height(x)
        bottom_height(x)
        x+=2
    elif k=='0':
        top_height(x)
        bottom_height(x)
        x+=1
        top_width(x)
        bottom_width(x)
        x+=s
        top_height(x)
        bottom_height(x)
        x+=2

for i in result:
    print(''.join(i))