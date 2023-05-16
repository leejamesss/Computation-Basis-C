n=int(input())
for _ in range(n):
    line=input()
    P_left=line.find("P=")+2
    P_right=line.find("W")

    U_left=line.find("U=")+2
    U_right=line.find("V")

    I_left=line.find("I=")+2
    I_right=line.find("A")


    P=1000000000000000
    U=1000000000000000
    I=1000000000000000

    if P_left==1 and P_right==-1:
        P=None
    if U_left==1 and U_right==-1:
        U=None
    if I_left==1 and I_right==-1:
        I=None


    if P!=None:
        P=float(line[P_left:P_right])
    if U!=None:
        U=float(line[U_left:U_right])
    if I!=None:
        I=float(line[I_left:I_right])


    if P!=None and U!=None:
        I=P/U
        #保留两位小数,用forrmat()函数
        I=format(I,'.2f')
        #输出
        print("Problem #"+str(_+1))
        print("I="+str(I)+"A")
        print()

    elif P!=None and I!=None:
        U=P/I
        U=format(U,'.2f')
        print("Problem #"+str(_+1))
        print("U="+str(U)+"V")
        print()

    elif U!=None and I!=None:
        P=U*I
        P=format(P,'.2f')
        print("Problem #"+str(_+1))
        print("P="+str(P)+"W")
        print()




    







      



