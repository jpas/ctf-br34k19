from random import getrandbits
from binascii import hexlify, unhexlify

e = 256
bound = 2^16

lg = lambda x: log(x, 2)

"""
(133033601991089115952160548971516482666207693057378474968624457876488851505152001, 2^17 * 3^9 * 5^3 * 7^6 * 11^6 * 13^2 * 19^6 * 31 * 37 * 53 * 59 * 61 * 73^2 * 79 * 103 * 109^2 * 127 * 157 * 337 * 547 * 593 * 1429 * 2099 * 11681 * 28921)
(13441226969039831665490833399257041550472758379859888875048830950549841174797, 2^2 * 7 * 23 * 63397 * 1773541251444588707485055736443 * 185627812052744052221838641547628193029)
1788134838871138072952098214386239776469370874299749353828617624074665756603926171121918624269492079935651419558425121489326252761210247140297007927895318797
(133033601991089115952160548971516482666207693057378474968624457876488851505152001, 13441226969039831665490833399257041550472758379859888875048830950549841174797)
"""

p = 133033601991089115952160548971516482666207693057378474968624457876488851505152001
q = 13441226969039831665490833399257041550472758379859888875048830950549841174797
N = p * q
E = 65537
d = Zmod((p - 1) * (q - 1))(E)^(-1)

def split_by_n(seq, n):
    while seq:
        yield seq[:n]
        seq = seq[n:]

def pretty(n, width=50):
    h = hex(ZZ(n))
    for s in split_by_n(h, width):
        print(s)

h = lambda x: hex(ZZ(x))

print('N:')
pretty(N)

m = ZZ('0x' + hexlify(b'br35k19{u53_5tr0ng_pr1m35}'))
#print('message:', h(m))

me = pow(m, E, N)
print('bob:')
pretty(me)
#print('encoded', h(me))

m_ = pow(me, d, N)
print('message', h(m_))

print(unhexlify(h(m_)))

"""
while ...:
    p = 1
    while lg(p + 1) < e:
        p *= getrandbits(16)

    p = p + 1
    if p in Primes():
        print(p, factor(p - 1))
        break


while ...:
    q = next_prime(getrandbits(e / 2))
    a = getrandbits(e / 2)

    q = a * q + 1
    if q in Primes():
        print(q, factor(q-1))
        break

print(p*q)
"""

def pollard(n, b):
    a = 2
    j = 2
    while j <= b:
        a = pow(a, j, n)
        d = ZZ(gcd(a - 1, n))
        if 1 < d < n:
            return d, n / d
        j += 1

print(pollard(N, bound))
