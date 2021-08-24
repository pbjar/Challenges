from Crypto.Util.number import *
# NOT DONE, FIX, EASILY WOLFRAMABLE

with open('flag.txt','rb') as f:
    flag = f.read().strip()

e=65537
p=getPrime(512)
q=getPrime(512)
n=p**3 + 2*p**2 q + 2*q**2 + p**2 - p*q**2 + 3*p*q - 2*q**3
m=bytes_to_long(flag)
ct=pow(m,e,n)


print (n)
print (e)
print (ct)
