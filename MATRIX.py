import sympy
import numpy

def main():
    switch=input('暗号化鍵で暗号化 -> 1  /  暗号化鍵で複合化 -> 2  /  鍵解読 (2x2の暗号文と平文が必要) -> 3\n')
    if switch == '1':
        mod=26# アルファベットのみなので thkkeykwow
        print('暗号化に使用する鍵を設定')
        key=setting()
        print('暗号化したい、アルファベットの平文を設定')
        P,m=multi()
        C=(key*P)%mod
        out(C,m)
    elif switch == '2':
        mod=26
        print('暗号化に使用する鍵を設定')
        key=setting()
        kinv=key.inv_mod(mod)
        print('暗号化したい、アルファベットの暗号化された文を設定')
        C,m=multi()
        P=(kinv*C)%mod
        out(P,m)
    elif switch == '3':
        print('暗号文の入力')
        C=setting()
        print('平文の入力')
        P=setting()
        mod=int(input('mod='))
        Pinv=P.inv_mod(mod)
        key=(C*Pinv)%mod
        print(key)
    else :
        print('')

def setting():
    
    print('[[a,b],[c,d]](mod n)')
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    d=int(input('d='))
    k=sympy.Matrix([[a,b],[c,d]])
    return k

def line():
    print('[[a,b],[c,d]](mod n)')
    a=str(input('a='))
    b=str(input('b='))
    c=str(input('c='))
    d=str(input('d='))
    a=ord(a)-97
    b=ord(b)-97
    c=ord(c)-97
    d=ord(d)-97
    k=sympy.Matrix([[a,b],[c,d]])
    return k

def multi():
    a1=str(input('文字入力、'))
    a2=([])
    for j in a1:
        aord=ord(j)-96
        a2.append(aord)
    n=int(len(a2))
    if (n%2)==1:
        a2.append(0)
    m=(len(a2)//2)# 2行m列
    a=numpy.array(a2)
    b=a.reshape(m,2)
    c=b.T
    A=sympy.Matrix(c)
    return A,m

def out(A:sympy.matrices.dense.MutableDenseMatrix , m:int):
    output=[]
    for x in range(m):
        for y in range(2):
            ins=A[y,x]+96
            if ins!=96:    
                ins=chr(ins)
                output.append(ins)
    output="".join(output)
    print(output)

def prerelease():
    m1=numpy.array([[2,4,56,2,3]])
    print(type(m1),m1.dtype)
    while(1):
        a=(input('暗号化したい文字を入力してください\n'))
        print(a,m1,a[1])
        m2=sympy.Matrix(m1)
        print(type(m2))
        if len(a)%2==1:
            print(m2)
        break

if __name__ == '__main__':
    main()