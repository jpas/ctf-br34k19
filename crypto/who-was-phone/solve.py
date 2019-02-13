#!/usr/bin/env python3
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

pt = '''
444d445e6044533e4f42463844794943514a4026444d422d59
456d2b785e4634503169454f58394f444d4c674d446f796b36
4429404b244471497231454a596f4e46385573464351497b56
43556f3e7044243c5268446f794c7d44524153214471497231
442164373445253e58714634505a72453742736844736d4f5e
456d2d4e4e442a32665046384356354351593f42454a5a7b64
4634503123454f48766544736d4f5e446f794c7d44524b4236
463523367d454a596f4e4638547e4c43514a4f6b45347b412a
4537366529446f796b36442a3266514523663f35444f603c48
434f323c634638546c3645387e642a444d4c6426446f794c7d
44524153214471497231443830585e434f323c6342296c4260
4539307c45444d422d5945725179704638532a2946357c3036
4426796b4b4523776a51463450312845347b423144736d5267
446f78656b4570687a374539307c45444d4547604352785244
'''

pt = ''.join(pt.split())

for d in (d16, rot13, d85, d64, d32, dphone):
    pt = d(pt)

print(pt.decode())
