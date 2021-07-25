"""
D=(a*d-b*c)%mod
x,y,z=sympy.gcdex(D,mod)
x=x%mod
print(x)
P=sympy.Matrix([[3,7,4],[9,2,6]])

"""

import sympy
import numpy

def main():
    switch=input('暗号化鍵で暗号化 -> 1  /  暗号化鍵で複合化 -> 2  /  鍵解読 (2x2の暗号文と平文が必要) -> 3\n')
    if switch == '1':
        key,mod=setting()
        print('')
    elif switch == '2':
        print('暗号文')
        reading()
    elif switch == '3':
        print('暗号文')
    else :
        print('')

def setting():
    
    print('[[a,b],[c,d]](mod n)')
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    d=int(input('d='))
    mod=int(input('mod='))
    k=sympy.Matrix([[a,b],[c,d]])
    return k,mod

def reading():
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

"""
def decrypt():
    k_inv=k.inv_mod(mod)#何故かこれは正常に動く。
    print(k)
    C=k_inv*P
    print(C)

"""
if __name__ == '__main__':
    main()