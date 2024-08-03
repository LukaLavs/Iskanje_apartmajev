#problem 1: Multiples of 3 or 5 (rešitev = 233168)
def multiplesof(a, b, obsegmax):
    st = 0
    for i in range(1,obsegmax):
        if i % a == 0 or i % b == 0:
            st += i
    return st
#print(multiplesof(3, 5, 1000))
###########################################################
#problem 2: Even Fibbonaci Numbers (rešitev = 4613732)
def fibonaci_naslednji(x1, x2):
    return x1 + x2
def even_fibonaci_number(obsegmax):
    a, b = 1, 2
    st = 0
    while a <= obsegmax:
        if a % 2 == 0:
            st += a
        a, b = b, a + b
    return st
#print(even_fibonaci_number(4000000))
#########################################################
#problem 3: Largest Prime Factor (rešitev = 6857)
def largest_prime_factor(n):
    faktorji = []
    while n % 2 == 0:
        faktorji.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            faktorji.append(i)
            n //= i
    if n > 2:
        faktorji.append(n)
    return max(faktorji)            
#print(largest_prime_factor(600851475143))
##################################################################
#problem 4: Largest Palindrome Product (rešitev = 906609)
def is_palindrome(n):
    for i in range((len(str(n)) // 2) + 1):
        if str(n)[i] != str(n)[-(i + 1)]:
            return False
    return True
def largest_palindrome_product():
    seznam = []
    for i in range(100, 999 + 1):
        for j in range(100, 1000):
            if is_palindrome(i * j):
                seznam.append(i * j)
    return max(seznam)
#print(largest_palindrome_product())
#########################################################
#problem 5: Smallest Multiple (rešitev = 232792560)
def smalest_multiple(n):
    deli = 0
    stevilo = 2 * n
    while True:
        stevilo += 1
        for i in range(1, n + 1):
            if stevilo % i == 0:
                deli += 1
        if deli == n:
            return stevilo
        deli = 0
#print(smalest_multiple(20))
#######################################################
#problem 6: Sum Square Difference (rešitev = 25164150)
def sumsquared_minus_sumofsquares(n):
    sumofsquares = 0
    sum = 0
    for i in range(1, n + 1):
        sumofsquares += i ** 2
    for i in range(1, n + 1):
        sum += i
    return sum ** 2 - sumofsquares
#print(sumsquared_minus_sumofsquares(100))
#########################################################
#problem 7: 10001st Prime (rešitev = 104743)
def ali_je_pra(n):
    if n <= 1 or (n % 2 == 0 and n != 2):
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
def n_th_prime(n):
    # ne deluje za n = 1
    stevilo_prastevil = 1
    x = 1
    while stevilo_prastevil < n:
        x += 2
        if ali_je_pra(x):
            stevilo_prastevil += 1         
    return x
def prastevila_do(n):
    if n < 2:
        return []

    prastevila = []
    je_pra = [True] * (n + 1)
    je_pra[0] = je_pra[1] = False
    for i in range(2, int(n**0.5) + 1):
        if je_pra[i]:
            for j in range(i * i, n + 1, i):
                je_pra[j] = False
    for i in range(2, n + 1):
        if je_pra[i]:
            prastevila.append(i)
    return prastevila
#print(n_th_prime(10001))
#########################################################
#######################################################
#problem 8 (rešitev = 23514624000)
text = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""
def trinajst(n):
    t = [int(s) for s in text if not s == "\n"]
    p = 0
    z = []
    for i in range(len(t)-n+1):
        r = 1
        for u in t[i:i + n]:
            r*=u
        if r > p:
            p = r
            z = t[i:i + n]
    f = 1
    for u in z:
            f*=u
    return f
#print(trinajst(13))
####################################################################
#problem 9: Special Pythagorean Triplet (trojica = 200, 375, 425, rešitev = 31875000)
def special_pythagorean_triplet():
    for a in range(1, 334):  # Ker je a naj bo a najmanjši.
        for b in range(a + 1, (1000 - a) // 2):  # ker b < c
            c = 1000 - a - b  #a + b + c = 1000
            if a * a + b * b == c * c:
                return a * b * c
#print(special_pythagorean_triplet())
#########################################################
#problem 10: Summation of Primes (rešitev = 142913828922)
def summation_of_primes(n):
    sum = 2
    for i in range(3, n + 1, 2):
        if ali_je_pra(i):
            sum += i
    return sum
#print(summation_of_primes(2000000))
###########################################################
#from sympy import divisors
#problem 12: Highly devisible triangle number (rešitev76576500)
def triangular_devisors():
    n = 1
    while True:
        t = n*(n+1)//2
        n += 1
        if len(divisors(t)) > 500:
            return t
#print(triangular_devisors())
##############################################
#problem 13: Large sum: resitev=5537376230
stevilo = """37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690"""
#print(str(sum(map(int,stevilo.split("\n"))))[:10]) 
#########################################################
#problem 14: (rešitev: 837799)
def collatez(n):
    r = 1
    while n != 1:
        r += 1
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n + 1
    return r
def longest_collatez(n):
    r = 2
    col_p = 1
    for i in range(3, n+1):
        f = collatez(i)
        if f > col_p:
            r = i
            col_p = f
    return r
#print(longest_collatez(1000000))    
########################################################
#problem 16: Power digits sum rešitev=1366
def power_digits(n):
    n = str(n)
    return sum([int(j) for j in n])
#print(power_digits(2**1000))    
#################################################
#problem 18 rešitev=1074
trikotnik="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def seznam():
    t = trikotnik.split("\n")
    t = [u for u in t if u != ""]
    t = [list(map(int, u.split(" "))) for u in t]
    return t
def flatten(gnezden_list):
    r = []
    for element in gnezden_list:
        if isinstance(element, list):
            r.extend(flatten(element))
        else:
            r.append(element)
    return r
def p(sez, i=0, z=0):
    if len(sez) == 1:
        return z + sez[0][i]
    return [p(sez[1:], i, sez[0][i]+z), p(sez[1:], i+1, sez[0][i]+z)]
def g(sez):
    r = []
    r.append(p(sez))
    return r
#print(max(set(flatten(g(seznam())))))
#################################################
#problem 20: factorial digit sum, rešitev =  648
def fakulteta(n):
    if n <= 1:
        return 1
    else:
        return fakulteta(n-1)*n
def fact_sum(n):
    return power_digits(fakulteta(n))
#print(fact_sum(100))
###################################################
#problem 25: 1000digits Fibonaci rešitev=4782
def fibo():
    a, b = 1, 1
    i = 2
    while b < 10**999:
        a, b = b, a+b
        i += 1
    return i
#print(fibo())
#############################################
#problem 27 rešitev= -59231
#b prime ker zacnemo z n=0, abs <1000
def quadratic_primes():
    def formula(n, a, b):
        return n**2 + a*n + b
    kandidatb = prastevila_do(1000)
    pra = prastevila_do(10000)
    print("kkk")
    def zaporedni(a, b):
        i = 0
        n = 0
        while formula(n, a, b) in pra:
            i += 1
            n += 1
        return i
    m = 0

    for a in range(-999, 1000):
        for b in kandidatb:
            r = zaporedni(a, b)
            if r > m:
                m = r
                konec = [a, b]
                
    return m, konec
#(71, [-61, 971]) = (zaporedna pra, [a, b])
#print(quadratic_primes())    
#####################################################
#problem 29: distinct Powers rešitev=9183
def distinct_powers():
    s = [i for i in range(2, 101)]
    r = []
    for a in s:
        for b in s:
            r.append(a**b)
    return len(set(r))
#print(distinct_powers())
##################################################################################
#problem 34 rešitev=40730
def fakulteta(n):
    if n <= 1:
        return 1
    return n*fakulteta(n-1)
def digits_fakulteta(n):
    return sum([fakulteta(int(i)) for i in str(n)])
def test():
    t=[]
    for i in range(3, 500000):
        if i == digits_fakulteta(i):
            t.append(i)
    return t
#print(test())
#[145, 40585]
######################################################
#problem 37: rešitev = 748317
#pra = prastevila_do(1000000)
def truncatable(n): 
    
    del1 = n 
    del2 = 0  
    while del1: 
        zadnji_del1 = del1 % 10; 
        del2 = del2 * 10 + zadnji_del1; 
        # 7 3797 
        # 97 379 
        # 797 37 
        # 3797 3 
        if int(str(del2)[::-1]) in pra and del1 in pra: 
            del1 //= 10 
        else:
            return False 

    return True
#r = []
#for j in pra:
    #if truncatable(j):
        #r.append(j)
#print( r, sum(r[4:]))

#print(truncatable(739397))
#[2, 3, 5, 7, 23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397] , 748317
#########################################################
# Number Splitting (rešitev = ) ni rešeno
from itertools import combinations

def moznosti(n):
    n = str(n)
    l = len(n)
    r = set()
    for i in range(1, l + 1):
        for comb in combinations(range(1, l), i - 1):
            deli = []
            prev = 0
            for i in comb:
                deli.append(int(n[prev:i]))
                prev = i
            deli.append(int(n[prev:]))
            r.add(sum(deli))
    return r
def s_number(n):
    j = n**(1/2)
    #if j != int(j):
       # return False
    if j in moznosti(n):
        return True
    else:
        return False
def t_number():
    k = [j**2 for j in range(1000000+1)]
    
    s = 0
    for i in k:
        if s_number(i):
            s += i
    return s

#########################################################

#########################################################################################################
#SOP and POS ni rešeno
def sum_of_products(vektor1, vektor2):
    sum = 0
    for i in range(len(vektor1)):
        sum += vektor1[i] * vektor2[i]
    return sum

def product_of_sums(vektor1, vektor2):
    product = 1
    for i in range(len(vektor1)):
        product *= (vektor1[i] + vektor2[i])
    return product

def subset(s):
    subsets = []
    n = len(s)
    for i in range(1 << n):
        subset = [s[j] for j in range(n) if (i & (1 << j))]
        subsets.append(subset)
    return subsets

def set_stevil_do_n(n):
    sez = []
    for i in range(1, n+1):
        sez.append(i)
    return sez

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_of_lists(sez):
    if not sez:
        return 1
    pra = prastevila_do(sez[-1])
    if sez[-1] in pra:
        return sez[-1]           
    result = sez[0]
    for st in sez[1:]:
        result = lcm(result, st)
    return result

def sum_of_lcm(S):
    sum = 0
    for sez in S:
        sum += lcm_of_lists(sez)
    return sum

#print(sum_of_lcm(subset(set_stevil_do_n(20))))
            
        
        
        
#####################################################
#problem 41 (rešitev = 7652413)
import random
#miller algoritem najden na spletu
def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    # Write n as d*2^r + 1 with d odd
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

from itertools import permutations
def pandigital_numbers(niz):
    digits = niz #niz='987654321'
    pandigital_numbers = [''.join(p) for p in permutations(digits)]
    return sorted(pandigital_numbers, reverse=True)

def pan_digits(n):
    niz = str(n)
    j = len(niz)
    return set(niz) == set('123456789'[:j])
def pan_prime():
    for h in ["123456789", "12345678", "1234567", "123456", "12345"]:    
        p = pandigital_numbers(h)
        print("ok")
        for i in range(0, len(p)):
            if miller_rabin(int(p[i])):
                return p[i]

#print(pan_prime())       
####################################################
#problem 44, Pentagon numbers (Rešitev: 5482660)
def pentagon():
    pentagon = [n * (3*n - 1)/2 for n in range(1, 5000)]
    for i in range(len(pentagon)-1):
        for j in range(i+1, len(pentagon)):
            if pentagon[i] + pentagon[j] in pentagon[j:] and abs(pentagon[i] - pentagon[j]) in pentagon[:j]:
                return pentagon[i], pentagon[j]
    return None
#(1560090.0, 7042750.0)
#D = 5482660
#print(pentagon())
################################################
#problem 45 (rešitev = 1533776805)
def triangular(k):
    e = []
    f = []
    t = [n*(n+1)/2 for n in range(1,k)]
    p = [n*(3*n-1)/2 for n in range(1,k)]
    h = [n*(2*n-1) for n in range(1,k)]
    print("ok")
    for z in t:
        if z in p:
            e.append(z)
            print("yes")
    for z in e:
        if z in h:
            f.append(z)
    return f
    
#print(triangular(100000))
#####################################################
#problem 46, Goldbachs Conjecture (rešitev = 5777)
def ali_kompozit(n):
    if n <= 3:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

def odd_kompozit(limit):
    odd_k = []
    for num in range(3, limit + 1, 2):
        if ali_kompozit(num):
            odd_k.append(num)
    return odd_k

def goldbach(t):
    x = True
    compositi = odd_kompozit(t)
    pra = prastevila_do(t)
    print("ok")
    for i in compositi:
        if x:    
            x = False
            for p in pra:
                if p < i:
                    t = (i - p)/2
                    if t > 0:
                        f = t**(1/2)
                        if f == int(f):
                            x = True
                    else:
                            x = True
        else: 
            return compositi[compositi.index(i)-1]
#print(goldbach(1500000))
############################################################
#problem 48: (rešitev: 9110846700)
def self_powers(n):
    return sum([a**a for a in range(1, n+1)])
#print(self_powers(1000))
##########################################################
#problem 49: Prime Permutations (rešitev = [2969, 6299, 9629] oziroma 296962999629)
def prime_permutation(najvec):
    prastevila = prastevila_do(najvec)
    
    permutirani = []
    for i in range(len(prastevila)//2):
        cifre_prastevila_i = sorted(str(prastevila[i]))
        for j in range(len(prastevila)//2, len(prastevila)):
            if sorted(str(prastevila[j])) == cifre_prastevila_i:
                vrednost = False
                for blok in permutirani:
                    
                    if prastevila[i] in blok:
                        indeks = permutirani.index(blok)
                        blok.append(prastevila[j])
                        vrednost = True
                        
                if vrednost == False:
                    permutirani.append([prastevila[i], prastevila[j]])
    # permutirani je list števil, ki so pra, in imajo enake števke

    seznam_sekvenc = []
    for blok in permutirani:
        for i in range(len(blok)-1):
            for j in range(i+1, len(blok)):
                dolzina = blok[j] - blok[i]
                for _ in range(j, len(blok)): #od j naprej
                    if blok[j] + dolzina in blok:
                        indeks = blok.index(blok[j] + dolzina)
                        seznam_sekvenc.append([blok[i], blok[j], blok[indeks]])
                    else:
                        break
    #imamo seznam_sekvenc, ki vsebuje končni odgovor, le da se pojavi večkrat
    
    result = []
    for blok in seznam_sekvenc:
        if not blok in result:
            result.append(blok)
        
    return result
#print(prime_permutation(9999))
# za hec, števila, ki so pra, z največ 5 števkami, ki imajo iste števke, in iste razdalje:
# [80191, 89101, 98011], [92381, 92831, 93281], [68713, 78163, 87613], [71947, 74719, 77491], [14821, 48121, 81421], 
# [61487, 64817, 68147], [78941, 84179, 89417], [14897, 47189, 79481], [76819, 81769, 86719], [18503, 51803, 85103], 
# [18593, 51893, 85193], [62773, 67723, 72673], [25087, 52807, 80527], [62597, 65927, 69257], [25793, 59273, 92753], 
# [25981, 59281, 92581], [26597, 59627, 92657], [67829, 68279, 68729], [29669, 62969, 96269], [60373, 63703, 67033], 
# [32969, 63299, 93629], [35671, 53617, 71563], [73589, 78593, 83597], [37561, 51637, 65713], [83987, 88937, 93887], 
# [88937, 93887, 98837], [89387, 93887, 98387], [63499, 63949, 64399], [49547, 54497, 59447]           
#######################################################################################################################        
#problem 50: Consecutive Prime Sum (rešitev = 997651) 
def consecutive_prime_sum(najvec):
    prastevila = prastevila_do(najvec)
    stevila = []
    seznam = [0]
    sestevek = 0
    i = 0
    for j in range(len(prastevila)):
        counter = 0
        while sestevek + prastevila[i] <= najvec:
            sestevek += prastevila[i]
            i += 1
            counter += 1       
        if ali_je_pra(sestevek):          
            if counter > seznam[-1]:
                seznam.append(counter)
                stevila.append(sestevek)
        counter = 0
        sestevek = 0
        i = j
    return stevila
#print(consecutive_prime_sum(1000000))  
#############################################################
#problem 53: Combinatoric Selections: rešitev = 4075
#import math
def selections():
    s = 0
    for n in range(1, 101):
        for r in range(0, n+1):
            komb = math.comb(n, r)
            if komb > 1000000:
                s += 1
    return s
#print(selections())
########################################################################
#problem 67: rešitev = 7273 
with open(r"c:\Users\lavse\Desktop\tutoriali\python\0067_triangle.txt", 'r') as file:
    v = file.readlines()
trikotnik = [list(map(int, u.split())) for u in v]

def max_pot2(triangle):
    for v in reversed(range(len(triangle) - 1)):
        for s in range(len(triangle[v])):
            triangle[v][s] += max(triangle[v + 1][s], triangle[v + 1][s + 1])

    return triangle[0][0]
#print(max_pot2(trikotnik))
    




    
