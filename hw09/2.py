x=int(input())
m=int(input())
sum=x
flag=0
#第一年
if x>=m:
    print(1)
else:
    for i in range(2,101):
        x=x*1.08
        sum=sum+x
        m=m*1.1
        if sum>=m:
            print(i)
            flag=1
            break
    if flag==0:
        print("Forget it.")
