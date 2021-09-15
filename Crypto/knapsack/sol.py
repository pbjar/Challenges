from Crypto.Util.number import inverse, GCD
from itertools import product
from ast import literal_eval

#vars

f = open('./output.txt', "r")
b = literal_eval(f.readline().split(': ')[1].strip())
c = int(f.readline().split(': ')[1].strip())

n, k = len(b), 20

#exploit

#leak r and then most of w due to bad q

r = 0
for i in b[:-k]:
    r = GCD(r, i)

w = [i // r for i in b[:-k]]

#brute force last k chars and normal decrypt rest

for i in product(range(2), repeat = k):
    cc = c
    for j in range(k):
        cc -= b[-k + j] * i[j]

    if cc % r == 0:
        cc //= r

        flg = [0] * (n - k) + list(i)
        for j in reversed(range(n - k)):
            flg[j] = cc // w[j]
            cc -= w[j] * flg[j] 

        flagbits = ''.join('0' if i == 0 else '1' for i in flg)

        try: 
            flag = int(flagbits, 2).to_bytes((n >> 3) + 1, 'big').decode('ascii') 
            print(flag)
        except:
            pass
