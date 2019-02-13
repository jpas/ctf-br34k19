from binascii import unhexlify

N = '''
855d7d0701e5ee74cb38ebb9a7eb22599a331860218cd42857
f95baeb3dbb9e3636665f91f39ef98712629c3b524c1b6d2de
2fe5ddcd59af981b0730ab16bce10d
'''
N = ZZ('0x' + ''.join(N.split()))
E = 65537

M = '''
dfb0ec5822e54c6471de28eaad2791b675d330e4cba3269f85
5c49005244e5b174c5aa3461d8d5ea5db5160c736cc5b6d774
c0c77c7496fcd799663c6ad91fd0f
'''
M = ZZ('0x' + ''.join(M.split()))

def pollard(n, b):
    a = 2
    j = 2
    while j <= b:
        a = pow(a, j, n)
        d = ZZ(gcd(a - 1, n))
        if 1 < d < n:
            return d, n / d
        j += 1

p, q = pollard(N, 2^16)

Fe = Zmod((p-1)*(q-1))

d = Fe(E)^(-1)

m = ZZ(pow(M, d, N))

print unhexlify(hex(m))
