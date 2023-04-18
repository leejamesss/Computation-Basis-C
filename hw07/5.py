
def isverticleTriangle(a,b,c):
    if a*a+b*b==c*c:
        return True
    else:
        return False

def isTriangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

def findverticleTriangle(a,b,c):
    if isTriangle(a,b,c):
        if isverticleTriangle(a,b,c) or isverticleTriangle(a,c,b) or isverticleTriangle(b,c,a):
            return True
        else:
            return False
    else:
        return False
n=int(input())
lst=[]
for i in range(1,n+1):
    for j in range(1,i):
        for k in range(1,j):
            if findverticleTriangle(i,j,k) and isTriangle(i,j,k):
                lst.append([k,j,i])
print(len(lst))
lst.sort(key=lambda x:(x[0],x[1],x[2]))
for i in lst:
    a,b,c=i[0],i[1],i[2]
    print(str(a)+"²"+"+"+str(b)+"²"+"="+str(c)+"²")
    
