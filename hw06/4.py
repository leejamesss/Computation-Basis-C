def isnum(n):                   #判断是否为质数
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def iscousin(n):                #判断是否为孪生素数
    if isnum(n) and isnum(n+2):
        return True
    return False


def printcousin(N,M):           #打印孪生素数
    if N==1:
        N=3
    for i in range(N,M):
        if i+2>M:               #超出范围
            break
        if iscousin(i):
            print(i,i+2,sep=';')

N,M=map(int,input().split(":")) #
#N,M大小排序
if N>M:
    N,M=M,N
printcousin(N,M)
