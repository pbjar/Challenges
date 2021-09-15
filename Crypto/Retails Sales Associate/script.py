from Crypto.Util.number import *


with open('flag.txt','rb') as f:
    flag = f.read().strip()

e=65537
p=getPrime(512)
q=getPrime(512)
n=p*q
m=bytes_to_long(flag)
ct=pow(m,e,n)


print (p)
print (q)
print (e)
print (ct)
