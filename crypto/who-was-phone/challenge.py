from base64 import b85encode as e85
from base64 import b64encode as e64
from base64 import b32encode as e32
from binascii import hexlify as e16

from base64 import b85decode as d85
from base64 import b64decode as d64
from base64 import b32decode as d32
from binascii import unhexlify as d16

def rot13(pt):
    A, Z, a, z = map(ord, 'AZaz')
    ct = bytearray(pt)
    for i, c in enumerate(ct):
        if A <= c <= Z:
            ct[i] = (c - A + 13) % 26 + A
        if a <= c <= z:
            ct[i] = (c - a + 13) % 26 + a
        pass
    return bytes(ct)

ephone_d = {
    '0': '0',
    '1': '1',
    '2': 'abc2',
    '3': 'def3',
    '4': 'ghi4',
    '5': 'jkl5',
    '6': 'mno6',
    '7': 'pqrs7',
    '8': 'tuv8',
    '9': 'wxyz9',
}

ephone_t = {}
for k, cs in ephone_d.items():
    x = 0
    for x, c in enumerate(cs, start=1):
        v = k * x
        if not c.isdigit():
            ephone_t[c.upper()] = v
        ephone_t[c] = v


def ephone(pt):
    pt = pt.decode()

    ct = []
    for c in pt:
        if c in ephone_t:
            ct.append(ephone_t[c])
        else:
            ct.append(c)

    return '.'.join(ct).encode()

def dphone(ct):
    ct = ct.decode().split('.')

    pt = []
    for c in ct:
        k = c[0]
        i = len(c) - 1
        if k.isdigit():
            pt.append(ephone_d[k][i])
        else:
            pt.append(c)

    return ''.join(pt).encode()

pt = b'br34k19{th15_15_cr4zy_50_c411_m3_m4yb3}'
ct = pt

for e in [ephone, e32, e64, e85, rot13, e16]:
    ct = e(ct)

def split_by_n(seq, n):
    while seq:
        yield seq[:n]
        seq = seq[n:]

def pretty(t, width=50):
    for s in split_by_n(t, width):
        print(s)


pretty(ct.decode())
