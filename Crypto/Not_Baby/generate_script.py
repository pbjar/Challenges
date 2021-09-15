# NOTE DO NOT PUT THIS SCRIPT INTO THE ACTUAL CTF

from Crypto.Util.number import *
'''
with open('flag.txt','rb') as f:
    flag = f.read().strip()'''
flag=b"flag"


p=getPrime(64)
q=getPrime(64)

c=3*p*q
b=7*q**2
a=15*p**2

e=65537
n=(a**3+b**3)-34*c**3

m=bytes_to_long(flag)
ct=pow(m,e,n)


print (n)
print (a+b+c)
print (a**2+b**2+c**2-(a*b+b*c+c*a))

print ()
print (p)
print (q)
