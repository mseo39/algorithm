def count(input_):
    num=input_.count('0')
    if(num==0):
        print('E')
    elif(num==1):
        print('A')
    elif(num==2):
        print('B')
    elif(num==3):
        print('C')
    elif(num==4):
        print('D')

a1=input()
a2=input()
a3=input()
count(a1)
count(a2)
count(a3)