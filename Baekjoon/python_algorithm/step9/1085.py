#직사각형에서 탈출
#x,y 좌표의 범위는 1 ≤ x ≤ w-1, 1 ≤ y ≤ h-1
#x,y좌표에서 직사각형 네변으로 직각으로 떨어지는 네개의 선중에 최소를 구하면 된다
x, y, w, h=map(int, input().split())
print(min(x,y,w-x,h-y))