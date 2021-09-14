with open("beescript.txt") as f:
    bmv = f.read().replace(" ", "\n").lower()

bad = ['!', '"', '#', '$', '%', '&', '0', '1', '2', '@', 'p', 'q']

with open("flag_checker.qasm") as f:
    lns = f.read().splitlines()

with open("prog.qasm", "wb") as f:
    ptr = 0
    for l in lns:
        for i in range(ptr, len(bmv)):
            if bmv[i] in bad:
                ptr = i+1
                break
            f.write(bmv[i].encode())
        if len(l) == 0:
            continue
        if l[0] == ';':
            continue
        tok = l.split()
        if tok[0] == 'MOV':
            if tok[2][0] != 'r':
                f.write(b'\x00' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2], 16)).encode())
            else:
                f.write(b'\x01' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2][1:], 16)).encode())
        if tok[0] == 'EXIT':
            f.write(b'\x02')
        if tok[0] == 'ADD':
            if tok[2][0] != 'r':
                f.write(b'\x10' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2], 16)).encode())
            else:
                f.write(b'\x11' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2][1:], 16)).encode())
        if tok[0] == 'SUB':
            if tok[2][0] != 'r':
                f.write(b'\x12' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2], 16)).encode())
            else:
                f.write(b'\x13' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2][1:], 16)).encode())
        if tok[0] == 'MUL':
            if tok[2][0] != 'r':
                f.write(b'\x14' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2], 16)).encode())
            else:
                f.write(b'\x15' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2][1:], 16)).encode())
        if tok[0] == 'DIV':
            if tok[2][0] != 'r':
                f.write(b'\x16' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2], 16)).encode())
            else:
                f.write(b'\x17' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2][1:], 16)).encode())
        if tok[0] == 'MOD':
            if tok[2][0] != 'r':
                f.write(b'\x18' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2], 16)).encode())
            else:
                f.write(b'\x19' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2][1:], 16)).encode())
        if tok[0] == 'NOT':
            f.write(b'\x20' + chr(int(tok[1][1:], 16)).encode())
        if tok[0] == 'AND':
            if tok[2][0] != 'r':
                f.write(b'\x21' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2], 16)).encode())
            else:
                f.write(b'\x22' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2][1:], 16)).encode())
        if tok[0] == 'XOR':
            if tok[2][0] != 'r':
                f.write(b'\x23' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2], 16)).encode())
            else:
                f.write(b'\x24' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2][1:], 16)).encode())
        if tok[0] == 'OR':
            if tok[2][0] != 'r':
                f.write(b'\x25' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2], 16)).encode())
            else:
                f.write(b'\x26' + chr(int(tok[1][1:], 16)).encode() + chr(int(tok[2][1:], 16)).encode())
        if tok[0] == 'EZ':
            f.write(b'\x30' + chr(int(tok[1][1:], 16)).encode())
        if tok[0] == 'LZ':
            f.write(b'\x31' + chr(int(tok[1][1:], 16)).encode())
        if tok[0] == 'GZ':
            f.write(b'\x32' + chr(int(tok[1][1:], 16)).encode())
        if tok[0] == 'JMP':
            if tok[1][0] != 'r':
                f.write(b'\x40' + chr(int(tok[1], 16)).encode())
            else:
                f.write(b'\x41' + chr(int(tok[1][1:], 16)).encode())
        if tok[0] == 'JF':
            if tok[1][0] != 'r':
                f.write(b'\x42' + chr(int(tok[1], 16)).encode())
            else:
                f.write(b'\x43' + chr(int(tok[1][1:], 16)).encode())
        if tok[0] == 'PUSH':
            if tok[1][0] != 'r':
                f.write(b'\x50' + chr(int(tok[1], 16)).encode())
            else:
                f.write(b'\x51' + chr(int(tok[1][1:], 16)).encode())
        if tok[0] == 'POP':
            f.write(b'\x52' + chr(int(tok[1][1:], 16)).encode())
        if tok[0] == 'POPN':
            f.write(b'\x53' + chr(int(tok[1][1:], 16)).encode())
        if tok[0] == 'EXL':
            if tok[1][0] != 'r':
                f.write(b'\x54' + chr(int(tok[1], 16)).encode())
            else:
                f.write(b'\x55' + chr(int(tok[1][1:], 16)).encode())
        if tok[0] == 'EXR':
            if tok[1][0] != 'r':
                f.write(b'\x56' + chr(int(tok[1], 16)).encode())
            else:
                f.write(b'\x57' + chr(int(tok[1][1:], 16)).encode())
        if tok[0] == 'MVL':
            if tok[1][0] != 'r':
                f.write(b'\x58' + chr(int(tok[1], 16)).encode())
            else:
                f.write(b'\x59' + chr(int(tok[1][1:], 16)).encode())
        if tok[0] == 'MVR':
            if tok[1][0] != 'r':
                f.write(b'\x5a' + chr(int(tok[1], 16)).encode())
            else:
                f.write(b'\x5b' + chr(int(tok[1][1:], 16)).encode())
        if tok[0] == 'GLEN':
            f.write(b'\x5c' + chr(int(tok[1][1:], 16)).encode())
        if tok[0] == 'SLEN':
            if tok[1][0] != 'r':
                f.write(b'\x5d' + chr(int(tok[1], 16)).encode())
            else:
                f.write(b'\x5e' + chr(int(tok[1][1:], 16)).encode())
        if tok[0] == 'QSUM':
            f.write(b'\x5f' + chr(int(tok[1][1:], 16)).encode())
        if tok[0] == 'LBL':
            f.write(b'\x60' + chr(int(tok[1], 16)).encode())
        if tok[0] == 'IN':
            f.write(b'\x70' + chr(int(tok[1][1:], 16)).encode())
        if tok[0] == 'OUT':
            f.write(b'\x71' + chr(int(tok[1][1:], 16)).encode())
    f.write(bmv[ptr:].encode())
