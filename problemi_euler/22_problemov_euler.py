#algoritem ki sem ga nekajkrat v naslednjih nalogah uporabljal
def prastevila_do_truelist(n):
    if n < 2:
        return []

    prastevila = []
    je_pra = [True] * (n + 1)
    je_pra[0] = je_pra[1] = False
    for i in range(2, int(n**0.5) + 1):
        if je_pra[i]:
            for j in range(i * i, n + 1, i):
                je_pra[j] = False
    return je_pra            



import random
#miller rabin algoritem je najden na spletu, uporabljen v nalogi
#ki uporablja funkcijo spirala2, in še eni nalogi
def miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    
    # Write n-1 as 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    
    # Perform k tests
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


#Koda je "grša" saj je bila pisana na telefonu


###############################################
#problem 15, resitev = 137846528820
def stej(x, y, spom=None):
    n = 20
    if spom is None:
        spom = {}
    if (x, y) in spom:
        return spom[(x, y)]
    if x == n or y == n:
        return 1
    if y < n and x < n:
        spom[(x, y)] = stej(x, y + 1, spom) + stej(x + 1, y, spom)
        return spom[(x, y)]
    return 0
###############################################
# problem 21, resitev =31626
import math

def delitelji(n):
    d = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)
    
def d(x):
    return sum(delitelji(x)[0:-1])  
    
def amicable():
    s = []
    memo={}
    keys = memo.keys()
    for i in range(1, 10001):
        memo[i] = d(i)
    for j in range(1, 10001):
        y = memo[j]
        if y!=j and y in keys:
            dy = memo[y]
            if dy == j:
                s.append(j)
    return s, sum(s)       
    
###############################################
# problem  11, resitev = 70600674

mreza = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""  

def product_mreza(n):
    global mreza
    mreza = [[int(i.lstrip("0")) if i != "00" else 0 for i in j.split(" ") ] for j in mreza.split("\n")]
    p = 0
    
    for i in range(n):
        for j in range(n):
            if i + 3 < n:
                t = 1
                for k in range(4):
                    t *= mreza[j][i + k]
                if t > p:
                    p = t
                    
            if j + 3 < n:
                t = 1
                for k in range(4):
                    t *= mreza[j + k][i]
                if t > p:
                    p = t
                    

            if i + 3 < n and j + 3 < n:
                t = 1
                for k in range(4):
                    t *= mreza[j + k][i + k]
                if t > p:
                    p = t

            if i - 3 >= 0 and j + 3 < n:
                t = 1
                for k in range(4):
                    t *= mreza[j + k][i - k]
                if t > p:
                    p = t
                    
    return p

###############################################
#problem 19 resitev 171
def prestopno(n):
    return (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)
    
def nedelja():
    s=0
    dnvi_msc = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dnevi = 0
    for leto in range(1901, 2000+1):
        for msc in range(1, 12+1):
            if dnevi%7==0:
                s+=1
            if msc==2 and prestopno(leto):
                dnevi += 29
            else:
                dnevi += dnvi_msc[msc-1]
    print(s)

###############################################
#problem 30 resitev=443839
def lastnost(n):
    s = 0
    m = n
    while n>0:
        s+=(n%10)**5
        n//=10
    if s==m:
        return True
    return False        
    
def fifth_powers():
    s = 1
    r =[]
    for i in range(10, 354294+1):
        if lastnost(i):
            r.append(i)
    print(sum(r), r)    

###############################################
#problem  28, resitev = 669171001
def spirala():
    s=1
    stevilo=1
    pristevek = 2
    dim = 1
    while dim < 1001:
        for _ in range(4):
            stevilo += pristevek
            s+=stevilo
        
        pristevek += 2   
        dim += 2
    return s     
       
##########################################$$$$
#problem 23, resitev=4179871
def nonabundant_sum():
    meja = 28123+1
    abundant = [i for i in range(1, meja) if d(i) > i]
    abundantsum = [i for i in range(1,meja)]
    for i in range(len(abundant)-1):
        for j in range(i, len(abundant)):
            i1 = abundant[i]
            j1= abundant[j]
            if j1 + i1 <meja:
                abundantsum[i1+j1-1] = 0
               
    print(sum(abundantsum))
###############################################
# problem 36, resitev=872187
def palindromic102(n):
    x = []
    while n>0:
        c,n= n%10, n//10
        x.append(c)
    
    return x[::-1] == x
    
def palindromic_in_bothabases():
    s=0
    for i in range(1, 10**6):
        if palindromic102(i) and palindromic102(int(bin(i)[2:])):
            s+=i
    return s    
# zanimivost, 19 je takih stevil    
###################################################
#problem 31, resitev=73682
s = 0
def coins(sez, target):
    global s
    if len(sez)==1:
        s+=1
    else:
        k=0
        while k*sez[-1] + 1 <= target or k*sez[-1] == target:
            if k*sez[-1] == target:
                s+=1
                k+=1
                if k*sez[-1] + 1 <= target:
                    
                    coins(sez[:-1],target-k*sez[-1])
                continue
                
            coins(sez[:-1],target-k*sez[-1])
            k+=1
    print(s)
#coins([1,2,5,10,20,50,100,200],200)   
#print(s) 
#################################################
#problem 35 resitev = 55
pra = prastevila_do_truelist(10**6)
def is_cilcular_prime(n):
    global pra
    l=len(str(n))-1
    if not pra[n]:
        return False
    for i in range(1,l+1):
        j,n = n%10,n//10
        n = j*10**(l) + n
        if not pra[n]:
            return False
    return True   
    
def undermilion():
    r=[]
    for i in range(10**6):
        if pra[i]:
            if is_cilcular_prime(i):
                r.append(i)   
    return r, len(r)                
#print(undermilion()) 
# za hec, vsa taka stevila   
#([2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377, 11939, 19391, 19937, 37199, 39119, 71993, 91193, 93719, 93911, 99371, 193939, 199933, 319993, 331999, 391939, 393919, 919393, 933199, 939193, 939391, 993319, 999331], 55)    
##########################################$$$$$$$    
 #problem 40, resitev = 210   
def dolzina():
    d=0
    x = 1
    r=1
    for n in range(1,600000):
        l=0
        g=n
        while n>0:
            l+=1
            n//=10
            d+=1
            if d%x==0:
                x*=10
                #print(d,g,l)
                r*=int(str(g)[l-1])
    return r  
#print(dolzina())               
###################################################
#problem 38, resitev=932718654
def pandigital_vprasaj(n):
    if 123456789>n or n>987654321:
        return False
    return set([i for i in str(n)]) == set(["1","2","3","4","5","6","7","8","9"])          
def panmultiples():
    r=[]
    for n in range(1,1000000):
        s=""
        for i in range(1,(n+1)*100):
            s+= str(i*n)
            if pandigital_vprasaj(int(s)):
                print(s,i,n) 
                r.append(s)
            if int(s)>987654321:
                break
    return sorted(r)[-1]            
####################################################
# problem 52, resitev=142857
def lastnost_permultip(n):
    t={i for i in str(n)}
    for i in range(2,6+1):
        if not t=={i for i in str(n*i)}:
            return False
    return True
def permultip():
    p =[]
    for i in range(1,1000000):
        if lastnost_permultip(i):
            p.append(i)
    print(p)          
#permultip()     
###############################################
#problem 56, resitev = 972
def dgsum(n):
    r=0
    while n >0:
        r += n%10
        n//=10
    return r    
def powerful_digsum():
    r = 0
    for a in range(1,100):
        for b in range(a, 101):
            p=dgsum(a**b)
            if p > r:
                r = p
                dod=(a,b)
            q=dgsum(b**a)
            if q>r:
                r=q
                dod=(b,a)
                
    print(r,dod)
#najvecji sum da stevilo, (99, 95) torej 99**95    
#powerful_digsum()  
################################################
#problem 63 resitev=49
def stdigits(n):
    r=0
    while n>0:
        n//=10
        r+=1
    return r    
def powerfuldigitssum():
    s=0
    for a in range(1,10):
        u=round(1/(1-math.log(a,10)))
        # meja izhaja iz a^n<10^(n-1),
        # po meji ima a^n manj kot n cifer 
        for b in range(1, u+1):
            p=a**b
            if stdigits(p)==b:
                s+=1
    print(s)
#powerfuldigitssum()
#######################$$####$$$$$$###########
# naiven pristop k nalogi 792, ni reseno
def v(n):
    r=0
    while True:
        if n%2==0:
            r+=1
            n//=2
        else:
            break    
    return r
    
def S(n):
    s=0
    for i in range(1,n+1):
        s+=math.comb(2*i,i)*(-2)**i    
    return s
    
def u(n):
    return v(3*S(n)+4)
    
def U(N):
    s=0
    for k in range(1,N+1):
        s+=u(k**3)
    return s
    
    
def U4(N,k):
    return u(k**N)
#print([u(i) for i in range(1,10)])            
    
#print(U(10))      
##############8282819282728288282828282882828######
#ni rešeno
#4503599627370517 je pra, slab algoritem
def eulercoin():
    s=0
    c= 1504170715041707+100
    for n in range(1,10**9):
        #cn= (1504170715041707*n)%4503599627370517
        cm= pow(1504170715041707*n, 1, 4503599627370517)
        #print(cn,cm)
        
        if cm < c:
            c = cm
            s += c
            print(c)
    print(s)
#eulercoin()  
##########################€€€€€€€€###############
#problem 92, resitev=8581146
#koda ni ravno hitra
def sekvenca_next(n):
    s=0
    while n>0:
        s += (n%10)**2
        n//=10
    return s
#print(sekvenca_next(10**7-1))             
def pridedo_osem(m):
    while True:
        if m==1:
            return False
        if m==89:
            return True
        m=sekvenca_next(m)
def resitev123():
    s = 0
    spomin={}
    for i in range(1,568):
        if pridedo_osem(i):
            spomin[i] = True
            s += 1
        else:
            spomin[i]= False    
    
    for i in range(568, 10**7):
        if spomin[sekvenca_next(i)]:
            s += 1
    return s
    
#print(resitev123())
#########€€€€€################№######## 
#problem 53, resitev = 26241
#miller rabin algoritem, prav tako kot v prvi datoteki
#dobljen na spletu
#k predstavlja tocnost millerjevega algoritma
def spirala2(k):
    pra = prastevila_do_truelist((10**6))
    print("ok")
    st_pra=0#s=1
    st_vsa=1
    stevilo=1
    pristevek = 2
    dim = 1
    procent=1
    while procent >= 0.1:
        for _ in range(4):
            stevilo += pristevek
            
            
            if stevilo < 1000000:
                if pra[stevilo]:
                    st_pra += 1
            else:
                if miller_rabin(stevilo, k):
                    st_pra += 1        
           
            
            st_vsa += 1    
        procent = st_pra/st_vsa   
        print(2222,st_pra,st_vsa,procent,dim)     
            
        
        pristevek += 2   
        dim += 2
    return procent, dim
#print(spirala2(5)) 

############€€€€72288282828282882###########
#problem 69, rešitev = 510510
#po formuli za phi pretvorimo problem v iskanje minimuma od
#produkt((1-1/p)) kjer p je pra in gre po razcepu za n 
def razcep(meja):
    r = [set() for _ in range(meja + 1)]
    
    for i in range(2, meja + 1):
        if not r[i]:
            for veckratnik in range(i, meja + 1, i):
                r[veckratnik].add(i)
    return r
    
def eulerfunction(meja):
    m=1000#kot neskoncno
    stevilo=None
    delitelj = razcep(meja)
    #print(delitelj)
    for i in range(2, meja):
        r=1
        for p in delitelj[i]:
            r*=(p-1)/p
           
        if r<m:
            m=r 
            stevilo=i
    print(stevilo, "funkcija:", 1/m)          
            
#eulerfunction(10**6)        
###########€€€€€#############################
#problem 144, resitev = 354
def ogledalo(a,c, x1, y1):
    if abs(x1) <= 0.01 and y1 > 0:
        return 0
    
    t = -(4*x1)/y1 #naklon tangente, premica pa je dana z ax+c
    #premica po zrcaljenju je anx+cn
    #normalo zamaknimo za kot med normalo in premico in poglejmo koeficient
    an = math.tan( 2*math.atan(-1/t) -math.atan(a) )
    cn = y1 - an*x1
    
    
    xn1 = ( 2*an*cn + ( (2*an*cn)**2 - 4*(-4-an**2)*(100-cn**2) )**0.5 ) / (-8 - 2*(an**2))   
    xn2 = ( 2*an*cn - ( (2*an*cn)**2 - 4*(-4-an**2)*(100-cn**2) )**0.5 ) / (-8 - 2*(an**2)) 
    
    if abs(xn1 - x1)<0.0001:
        #potem xn1 ni resitev
        yn2 = an*xn2 + cn
        print((round(xn2,3),round(yn2,3)))
        return 1 + ogledalo(an, cn, xn2, yn2) 
        
    else:
        yn1 = an*xn1 + cn
        print((round(xn1,3),round(yn1,3)))
        return 1 + ogledalo(an, cn, xn1, yn1)     
#print(ogledalo((-9.6-10.1)/1.4, 10.1, 1.4, -9.6))
############################################################
#problem 39, resitev = 840
#obseg 840 se pojavi v 8 razlicnih pravokotnih trikotnikih
def obseg():
    s=set()
    for i in range(1,501): #meja je 500 ker (x**2+1)**0.5 + 1 + x <= 1000
        for j in range(1,503-i):
            h = math.sqrt(i**2+j**2)
            if int(h)==h:
                if i<j:
                    s.add((i,j,h))
                else:
                    s.add((j,i,h)) 
    o=[]                
    for (a,b,c) in s:
        u =a+b+c
        if u<=1000:
            o.append(u)   
    #prestejmo se kateri obseg se pojavi najveckrat                       
    o=sorted(o)
    n=[0,0]
    prejsnji=None
    for i in o:
        if i == prejsnji:
            stevec+=1
            if stevec > n[0]:
                n = [stevec, i]
                prejsnji=i
        else:
            stevec=1  
            prejsnji=i
    print(n)      
#obseg()
################################################
#To je bilo 20 problemov
#problem 33, resitev=100
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
def lastnostdgcnc(a,b,c,d):
    if (not str(int(a)) in str(c)) or (not str(int(b)) in str(d)):
        return False
    x1,x2=None,None    
    for i,j in zip(str(c),str(d)):
        if i != str(int(a)):
            x1 = i
        if j != str(int(b)):
            x2 = j
            
    return x1==x2   
    
def digitscanceling():
    x,y=1,1
    for a in range(10,99):
        for b in range(a,100):
            if a!=b and not (a%10==0 and b%10==0) and not (a%11==0 and b%11==0):
                d = gcd(a,b)
                if d != 1 and a/d<10 and b/d<10:
                    if lastnostdgcnc(a/d,b/d,a,b):
                        #ulomki.append([(a/d,b/d),(a,b)])
                        x*=a 
                        y*=b
    #primnozimo se 49/98=4/8, tega algoritem ni nasel, saj 4/8 ni okrajsan ulomek
    #ostale 3 pa je nasel in vemo da so točno 4 taki ulomki                  
    x*=4
    y*=8                      
    d=gcd(x,y)
    return y/d
#print(digitscanceling())                
##############################################################
#problem 146, rešitev =676333270
#iz dejstva so prastevila liha, in da je stevilo deljivo z 5, ce ima
#za zadnjo cifro 5, ugotovimo da n**2%10==0 in zato n%10==0
#koda kljub temu ni ravno hitra
def zaporednapra():
    s=0
    M=150*10**6
    k=[1,3,7,9,13,27]
    
    for n in range(0,M,10):
        v=True
        N=n**2
        for j in k:
            if not miller_rabin(N+j,3):
                v=False
                break
        if v:    
            s+=n
            print(n)
    print("vsota:",s)
#zaporednapra() #ta koda je dala kandidate, ki pa ne dajo prave resitve, torej eno ali več izmed njih ne da zaporednih prastevil.      
kandidati= [
10,
315410,
927070,
2525870,
8146100,
16755190,
39313460,
97387280,
119571820,
121288430,
130116970,
139985660,
144774340] 
def preglejkandidate():
    s=0
    global kandidati
    for n in kandidati:
        N=n**2
        if not miller_rabin(N+11,4) and not miller_rabin(N+17,4) and not miller_rabin(N+19,4) and not miller_rabin(N+23,4) and not miller_rabin(N+21,4): 
            s+=n
            print(n)
    print("vsota:",s)
#preglejkandidate()
#############################################################