#40917=漢字最後 

#　エラー処理 tryとかexpect

# アルファベットは正常に動作するが、40917にすると異なる値が出てきてしまう、数値の設定が良くない可能性？
#40917モードで数字にすると小さい値、『、ab、あ、などは成功。abc、ああ、は失敗。計算上うまくいっていない部分があるかも？
#ハッシュソートが使えないパターンみたいに、被りが生じてしまう？
#->後日立証。n=120223x133039、e=140909で失敗する、ああ、で成功。abc失敗
#  -<のような入力不能な文字のせいで暗号化復号化で数値がずれる可能性？？
#-> n=725603x726853、e=729041、でabc成功。単純に数を増やせば正常に動く範囲が広くなるとほぼ確定した !!!!!
import sympy

def main():
    switch = int(input(' 暗号化 or 電子署名文の検証 -> 1  (アルファベット表記 -> 11 )  \n 復号化 or 電子署名 -> 2  (アルファベット表記 -> 22 ) \n素因数分解 (脆い公開鍵から秘密鍵を導く) -> 3 \n ==>>'))
    n=40917# 文字の種類の数、アルファベットは26,Unicord 漢字表記をすべて入れるため40917。
    if switch==11 or switch==22:
        n=26#アルファベット用
    print('N=',n)
    if switch ==1 or switch ==11:
        p1=str(input('暗号化 (署名検証) する文章を入力\n->'))
        mod=int(input('公開鍵 mod (n) を入力、'))#モジュロ演算に用いる数
        e=int(input('公開鍵 e を入力'))#互いに素である二つの数の積
        P=setting(n,switch,p1,mod,e)
        print(' ( 署名値== )',P)
        CP=crypt(P,n,switch)
        strCP="".join(CP)
        print('暗号化済みの文 \n',strCP)
    elif switch == 2 or switch==22:
        p1=str(input('復号化 (署名) する文章を入力\n->'))
        p=int(input('q='))
        q=int(input('q='))
        mod=p*q
        L=sympy.lcm(p-1,q-1)
        e=int(input('公開鍵 e を入力'))#  65537
        d,y,z=sympy.gcdex(e,L)
        d=d%L #dを最小生剰余に
        d=int(d)
        powed=setting(n, switch,p1,mod,d)#e->d
        post=crypt(powed,n,switch)
        strP="".join(post)
        print('最小公倍数の最小正剰余 L =',L,'  /  秘密鍵 d　=',d)
        print('元の文 or 署名済みの文\n',strP)
    elif switch == 3:
        fact()
    else :
        print('')

def setting(n: int, switch: int,p1: str,mod: int,e:int ) -> int :
    ii=1
    P=0
    for i in p1:
        ins=ord(i)
        if switch==11 or switch==22:
            ins=ins-97#a->0
        plen=len(p1)-ii
        ii+=1
        ins=ins*(n**plen)
        P=P+ins
        print(P,'\n',e,mod,n)
    powed=pow(P,e,mod)
    print(powed)
    return powed
    

def crypt(P: int,n: int,switch: int) -> list:
    p2=[]
    while(P!=0):
        ins1=P%n
        P=P//n
        if switch==11 or switch==22:
            ins1=ins1+97        
        ins1=chr(ins1)#未登録の数字が出てしまうと表記がおかしくなる。一応戻せる。
        p2.insert(0, ins1)
    return p2
    
def fact():
    n = int(input('n='))
    list=[]
    for i in range(2,n+1):
        while True:
            if n%i == 0:
                list.append(i) # 余り0なら素因数分解リストにappendする
                n = n//i # nの更新
                print(list)
                print("n={}".format(n)) # nの更新状況をみてみる
            else:
                break


if __name__ == '__main__':
    main()