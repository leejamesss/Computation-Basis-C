n=int(input())
primelst=[]
def isprime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def findprime(n):
    for i in range(2,n):
        if isprime(i):
            primelst.append(i)
    return primelst

lst=findprime(10000)
print(lst[n-1])
