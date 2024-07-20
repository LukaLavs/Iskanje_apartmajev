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
#problem 20: factorial digit sum, rešitev =  648
def fakulteta(n):
    if n <= 1:
        return 1
    else:
        return fakulteta(n-1)*n
def fact_sum(n):
    return power_digits(fakulteta(n))
#print(fact_sum(100))
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

    




    
