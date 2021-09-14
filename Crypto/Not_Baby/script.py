from Crypto.Util.number import *

with open('flag.txt','rb') as g:
    flag = g.read().strip()

with open('primes.txt','rb') as f:
	s=f.read().strip().split()
	p=int(s[0])
	q=int(s[1])


c=3*p*q
b=7*q
a=15*p

e=65537
n=34*c**3-(a**3+b**3)

m=bytes_to_long(flag)
ct=pow(m,e,n)


print ("n: ",n)
print ("e: ",e)
print ("ct: ",ct)
