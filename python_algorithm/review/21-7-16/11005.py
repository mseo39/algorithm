#진법변환2
tmp=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def convert(num, notation):
    a, b=divmod(num, notation)
    if(a==0):
        return tmp[b]
    else:
        return convert(a,notation) + tmp[b]
a, b=map(int, input().split())
print(convert(a,b))