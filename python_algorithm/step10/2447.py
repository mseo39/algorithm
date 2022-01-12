#
def func(n,i,s):
    s1=[]
    for k in s:
        s1.append(k*3)
    for k in s:
        s1.append(k+(" "*i)+k)
    for k in s:
        s1.append(k*3)

    if(n==i):
        for k in s:
            print(k)
        return 0
    func(n,i*3,s1)

s=["***","* *","***"]
func(int(input()),3,s)